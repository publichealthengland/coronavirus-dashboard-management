# Generated by Django 3.2.5 on 2021-09-02 09:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
# import gm2m.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('service_admin', '0043_auto_20210829_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('type', models.CharField(choices=[('chart', 'Chart'), ('multiAreaStatic', 'Multi area static'), ('recentData', 'Recent data'), ('ageSexBreakdown', 'Age-Sex breakdown'), ('ageSexBreakdown', 'Age-Sex breakdown'), ('simpleTableStatic', 'Simple table static')], max_length=25)),
                ('heading', models.CharField(max_length=75)),
                ('full_width', models.BooleanField(default=True)),
                ('optional_view', models.BooleanField(default=False)),
                ('abstract', models.TextField(null=True)),
                ('introduction', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'card',
                'db_table': 'cms"."card',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.card')"
        ),
        migrations.CreateModel(
            name='CustomFieldParameter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('key', models.CharField(max_length=120)),
                ('sign', models.CharField(choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('!=', '!=')], max_length=2)),
                ('value', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'custom field parameter',
                'db_table': 'cms"."custom_field_parameter',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.custom_field_parameter')"
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('id_label', models.CharField(blank=True, help_text='For internal use.', max_length=255, null=True)),
                ('label', models.CharField(max_length=40)),
                ('from_index', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(-30), django.core.validators.MaxValueValidator(-1)])),
                ('to_index', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(-29), django.core.validators.MaxValueValidator(0)])),
                ('colour', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
            ],
            options={
                'verbose_name': 'highlight',
                'db_table': 'cms"."highlight',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.highlight')"
        ),
        migrations.CreateModel(
            name='LocationFilter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('id_label', models.CharField(blank=True, help_text='For internal use.', max_length=255, null=True)),
                ('excluded', models.BooleanField(default=False)),
                ('area_types', models.ManyToManyField(to='service_admin.AreaPriorities', db_table='cms"."location_filter_locations')),
            ],
            options={
                'verbose_name': 'location filter',
                'db_table': 'cms"."location_filter',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.location_filter')",
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.location_filter_locations')",
        ),
        migrations.CreateModel(
            name='RollingAverage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('window', models.PositiveSmallIntegerField(default=7, help_text='Number of points included in the rolling average window - range: [2, 28]', validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(28)])),
                ('clip_end', models.PositiveSmallIntegerField(help_text='Number of points to exclude from the end (offset) - range: [1, 10]', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'verbose_name': 'rolling average',
                'db_table': 'cms"."rolling_average',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.rolling_average')"
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('id_label', models.CharField(blank=True, help_text='For internal use.', max_length=255, null=True)),
                ('type', models.CharField(choices=[('chart', 'Chart'), ('table', 'Table'), ('nestedTable', 'Nested table'), ('metadata', 'Metadata'), ('heatmap', 'Heatmap')], max_length=20)),
                ('label', models.CharField(max_length=40)),
                ('custom_parameters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_admin.customfieldparameter')),
            ],
            options={
                'verbose_name': 'tab',
                'db_table': 'cms"."tab',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.tab')"
        ),
        migrations.CreateModel(
            name='TabField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('field_id', models.UUIDField()),
                ('field_type', models.ForeignKey(limit_choices_to={'model__in': ['VisualisationField', 'TabulationField']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_admin.tab')),
            ],
            options={
                'verbose_name': 'tab field',
                'db_table': 'cms"."tab_field',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.tab_field')"
        ),
        migrations.CreateModel(
            name='TabulationField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('id_label', models.CharField(blank=True, help_text='For internal use.', max_length=255, null=True)),
                ('label', models.CharField(db_index=True, max_length=40)),
                ('type', models.CharField(choices=[('numeric', 'Numeric'), ('date', 'Date'), ('text', 'Text')], max_length=10, null=True)),
                ('tooltip', models.CharField(max_length=255, null=True)),
                ('nested_metrics', models.JSONField(max_length=20, null=True)),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_admin.metricreference')),
            ],
            options={
                'verbose_name': 'tabulation field',
                'db_table': 'cms"."tabulation_field',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.tabulation_field')"
        ),
        migrations.CreateModel(
            name='VisualisationField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique ID')),
                ('id_label', models.CharField(blank=True, help_text='For internal use.', max_length=255, null=True)),
                ('label', models.CharField(db_index=True, max_length=40)),
                ('type', models.CharField(choices=[('line', 'Line'), ('bar', 'Bar')], max_length=10, null=True)),
                ('colour', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('tooltip', models.CharField(max_length=255, null=True)),
                ('fill', models.PositiveSmallIntegerField(help_text='Only applicable to line (area) plots - leave blank for other types.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('bar_type', models.CharField(choices=[('overlay', 'Overlay'), ('group', 'Group'), ('stack', 'Stack')], help_text='Only applicable to bar plots - leave blank for other types.', max_length=20, null=True)),
                ('amplitude', models.CharField(max_length=20, null=True)),
                ('amplitude_label', models.CharField(max_length=20, null=True)),
                ('metric_label', models.CharField(max_length=20, null=True)),
                ('parameter', models.CharField(max_length=20, null=True)),
                ('nested_metrics', models.JSONField(max_length=20, null=True)),
                ('highlight', models.ForeignKey(help_text='Only applicable to bar plots - leave blanks for other types.', null=True, on_delete=django.db.models.deletion.CASCADE, to='service_admin.highlight')),
                ('rolling_average', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_admin.rollingaverage')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_admin.metricreference')),
            ],
            options={
                'verbose_name': 'visualisation field',
                'db_table': 'cms"."visualisation_field',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.visualisation_field')"
        ),
        migrations.RemoveField(
            model_name='content',
            name='child_of',
        ),
        migrations.RemoveField(
            model_name='content',
            name='page',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='content',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='field',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.AddField(
            model_name='tab',
            name='fields',
            field=models.ManyToManyField('service_admin.VisualisationField', 'service_admin.TabulationField', through='service_admin.TabField', through_fields=['tab', 'field', 'field_type', 'field_id']),
        ),
        migrations.AddField(
            model_name='card',
            name='location_aware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_admin.locationfilter'),
        ),
    ]
