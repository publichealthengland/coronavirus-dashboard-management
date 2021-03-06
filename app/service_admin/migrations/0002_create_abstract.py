# Generated by Django 3.1.7 on 2021-03-01 12:32

from django.db import migrations, models
import service_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "SET LOCAL citus.multi_shard_modify_mode TO 'sequential';"
        ),
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', service_admin.models.VarCharField(max_length=255)),
                ('abstract', models.TextField()),
            ],
            options={
                'db_table': 'covid19\".\"abstract',
            },
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('covid19.abstract')"
        )

    ]
