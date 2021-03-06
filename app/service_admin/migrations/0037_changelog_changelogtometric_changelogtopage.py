# Generated by Django 3.1.7 on 2021-07-06 13:00

from django.db import migrations, models
import markdownx.models
import service_admin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0036_auto_20210620_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('expiry', models.DateField(null=True)),
                ('heading', service_admin.models.fields.VarCharField(max_length=150)),
                ('body', markdownx.models.MarkdownxField()),
                ('details', markdownx.models.MarkdownxField(null=True)),
                ('high_priority', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'covid19"."change_log',
                'ordering': ('-date',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChangeLogToMetric',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'covid19"."change_log_to_metric',
                'ordering': ('log', 'metric'),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChangeLogToPage',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'covid19"."change_log_to_page',
                'ordering': ('log', 'page'),
                'managed': False,
            },
        ),
    ]
