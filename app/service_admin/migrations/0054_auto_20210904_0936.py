# Generated by Django 3.2.5 on 2021-09-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0053_auto_20210904_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tab',
            name='custom_parameters',
        ),
        migrations.AddField(
            model_name='tab',
            name='custom_filters',
            field=models.ManyToManyField(to='service_admin.CustomFilterParameter', db_table='cms"."tab_to_filters'),
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.tab_to_filters')"
        ),
    ]
