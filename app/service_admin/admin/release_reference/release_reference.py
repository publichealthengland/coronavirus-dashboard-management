#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
import re
import logging

# 3rd party:
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django.conf import settings

from azure.cosmosdb.table.tableservice import TableService

from reversion.admin import VersionAdmin

from django_object_actions import DjangoObjectActions

# Internal:
from . import actions, list_filters
from service_admin.models import ReleaseReference, ProcessedFile
from service_admin.admin.generic_admin import GuardedAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'ReleaseReferenceAdmin'
]


@admin.register(ReleaseReference)
class ReleaseReferenceAdmin(DjangoObjectActions, VersionAdmin, GuardedAdmin):
    try:
        table_obj = TableService(connection_string=settings.ETL_STORAGE)
    except ValueError as err:
        logging.error(err)

    date_hierarchy = 'timestamp'

    search_fields = ('label',)
    list_per_page = 30
    readonly_fields = ["category"]
    changelist_actions = [
        'purge_storage_cache',
        'repopulate_cache',
        'flush_despatch_cache',
        'flush_all_cache',
    ]
    actions = [
        actions.release_selected,
        actions.recalculate_selected_count,
        actions.reset_release_stats,
        actions.reporocess_release,
    ]
    list_filter = [
        list_filters.FilterByReleaseStatus,
        list_filters.FilterByReleaseCategory,
        ('timestamp', list_filters.DateTimeFilter)
    ]

    list_display = [
        'id',
        'formatted_release_time',
        'average_ts',
        'category',
        'etl_status',
        'count',
        'delta',
        'released',
        'despatch_time'
    ]

    list_display_links = [
        'formatted_release_time'
    ]

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'timestamp',
                    'released',
                    'category'
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return request.user.is_superuser

    def formatted_release_time(self, obj):
        return mark_safe(obj.timestamp.strftime("%a, %d %b %Y &ndash; %H:%M:%S"))

    formatted_release_time.admin_order_field = 'timestamp'
    formatted_release_time.short_description = 'receipt time'

    def despatch_time(self, obj):
        try:
            return obj.despatch_of.order_by("-timestamp").last()
        except (ValueError, AttributeError):
            return None

    despatch_time.admin_order_field = 'despatch time'
    despatch_time.short_description = 'despatch time'

    def average_ts(self, obj):

        file_path = static(
            re.sub(
                r"[:\s'\"&]+",
                "_",
                f'releases/{obj.category.process_name}/{obj.timestamp:%Y-%m-%d}.png'
            )
        )

        return mark_safe(
            f'<img src="{file_path}" loading="lazy" width="180" '
            f'style="margin-top: -10px; margin-bottom: -10px;"/>'
        )

    average_ts.admin_order_field = 'Relative receipt time'
    average_ts.short_description = 'Relative receipt time'

    def etl_status(self, obj):
        try:
            process_id = (
                ProcessedFile
                .objects
                .filter(release=obj.id)
                .order_by("timestamp")
                .last()
                .process_id
            )
        except AttributeError:
            return None

        data = self.table_obj.query_entities(
            settings.ETL_STORAGE_TABLE_NAME,
            filter=f"PartitionKey eq '{process_id}'",
        )

        for task in data:
            if task.RuntimeStatus == 'Completed':
                return mark_safe(f'<strong style="color: #074428">{task.RuntimeStatus}</strong>')
            elif task.RuntimeStatus == 'Running':
                return mark_safe(f'<strong style="color: #000044">{task.RuntimeStatus}</strong>')
            elif task.RuntimeStatus == 'Failed':
                return mark_safe(f'<strong style="color: #900000">{task.RuntimeStatus}</strong>')
            else:
                return task.RuntimeStatus

    etl_status.admin_order_field = 'ETL Status'
    etl_status.short_description = 'ETL Status'

    def flush_all_cache(self, request, obj):
        return actions.flush_all_cache(self, request, obj)

    flush_all_cache.label = "Flush all cache"
    flush_all_cache.short_description = "Instantly flush all cache"

    def flush_despatch_cache(self, request, obj):
        return actions.flush_despatch_cache(self, request, obj)

    flush_despatch_cache.label = "Flush despatch cache"
    flush_despatch_cache.short_description = "Flush cache servers in serial"

    def repopulate_cache(self, request, obj):
        return actions.repopulate_cache(self, request, obj)

    repopulate_cache.label = "Repopulate summary cache"
    repopulate_cache.short_description = "Repopulate cache for Summary pages"

    def purge_storage_cache(self, request, obj):
        return actions.purge_storage_cache(self, request, obj)

    purge_storage_cache.label = "Purge storage cache"
    purge_storage_cache.short_description = "Purge storage cache for APIv2 and Easy-Read pages"
