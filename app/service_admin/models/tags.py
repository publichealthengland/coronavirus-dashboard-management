#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:

# 3rd party:
from django.db import models, connection
from django.utils.translation import gettext as _

from django_multitenant import fields as mt_fields
from django_multitenant import models as mt_models
from django_multitenant import mixins as mt_mixins
from reversion import register as versioned

# Internal: 
from .fields import VarCharField
from .data import MetricReference
from ..utils.default_generators import generate_unique_id
from uuid import uuid4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


__all__ = [
    "Tag",
    "MetricTag"
]


class TenantManager(mt_models.TenantManagerMixin, models.Manager):
    pass


@versioned()
class Tag(models.Model):
    ASSOCIATION_CHOICES = [
        ("METRICS", _("Metrics")),
        ("CHANGE LOGS", _("Change Logs")),
    ]
    id = models.UUIDField(
        verbose_name=_("unique ID"),
        primary_key=True,
        editable=False,
        default=uuid4
    )
    association = VarCharField(max_length=30, null=False, blank=False, choices=ASSOCIATION_CHOICES)
    tag = VarCharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.tag

    class Meta:
        managed = False
        db_table = 'covid19"."tag'
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


@versioned()
class MetricTag(models.Model):
    id = models.UUIDField(
        verbose_name=_("unique ID"),
        primary_key=True,
        editable=False,
        default=uuid4
    )
    metric = models.ForeignKey(
        MetricReference,
        on_delete=models.CASCADE,
        to_field="metric",
        related_name='tag_of'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        limit_choices_to={"association": "METRICS"},
        related_name='metric_of'
    )

    def __str__(self):
        return self.tag.tag

    class Meta:
        managed = False
        db_table = 'covid19"."metric_tag'
        unique_together = [
            ('tag', 'id'),
            ('metric', 'tag')
        ]
        ordering = ('metric', '-tag')
