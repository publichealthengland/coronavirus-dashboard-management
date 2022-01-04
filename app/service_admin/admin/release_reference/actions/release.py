#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from datetime import datetime, timedelta
from json import dumps

# 3rd party:
from django.utils.translation import gettext as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, CHANGE, ADDITION, DELETION
from django.contrib import messages
from django.conf import settings

# Internal: 
from service_admin.models import Despatch, DespatchToRelease
from service_admin.utils.dispatch_ops import update_timestamps
from service_admin.utils.presets import ServiceName

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'release_selected'
]


SERVICE_NAME = getattr(ServiceName, settings.ENVIRONMENT)


def release_selected(modeladmin, request, queryset):
    if settings.DEBUG:
        return messages.success(request, _(f"This feature is unavailable in debug mode."))

    timestamp = datetime.utcnow()
    time_past_the_hour = timedelta(
        minutes=timestamp.minute,
        seconds=timestamp.second,
        microseconds=timestamp.microsecond
    )
    prev_hour = timestamp - time_past_the_hour
    next_hour = prev_hour + timedelta(hours=1)
    queryset.update(released=True)

    despatch = Despatch.objects.filter(timestamp__gte=prev_hour, timestamp__lte=next_hour).first()
    if despatch is None:
        despatch = Despatch.objects.create(timestamp=timestamp)

    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(despatch).pk,
        object_id=despatch.id,
        object_repr=timestamp.isoformat(),
        action_flag=ADDITION,
        change_message=dumps([
            {"category": "data despatched", "timestamp": timestamp.isoformat(), "released_object_id": str(release.id)}
            for release in queryset
        ])
    )

    new_objects = list()
    for release in queryset:
        old_releases = DespatchToRelease.objects.filter(release=release).all()
        for item in old_releases:
            category = item.release.category.process_name
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(item).pk,
                object_id=item.id,
                object_repr=str(item),
                action_flag=DELETION,
                change_message=dumps([{
                    "timestamp": item.release.timestamp.isoformat(),
                    "category": category,
                }])
            )
            item.delete()

        new_objects.append(DespatchToRelease(despatch=despatch, release=release))

        LogEntry.objects.log_action(
            user_id=request.user.id,
            content_type_id=ContentType.objects.get_for_model(release).pk,
            object_id=release.id,
            object_repr=str(release),
            action_flag=CHANGE,
            change_message=dumps([{
                "description": "despatched",
                "timestamp": timestamp.isoformat(),
                "category": release.category.process_name,
                "despatch_object_id": despatch.id
            }])
        )

    DespatchToRelease.objects.bulk_create(new_objects)

    update_timestamps(timestamp)

    return messages.success(request, _(f"Successfully released %d items.") % len(new_objects))


release_selected.short_description = _(f"Release selected items on {SERVICE_NAME.capitalize()}")
