# Generated by Django 3.1.7 on 2021-03-06 01:08

from django.db import migrations
import django.db.models.deletion
import django_multitenant.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0020_auto_20210306_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricasset',
            name='body',
            field=markdownx.models.MarkdownxField(),
        )
    ]
