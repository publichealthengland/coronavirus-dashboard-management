# Generated by Django 3.2.5 on 2021-08-07 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0041_auto_20210807_1125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BannerArea',
        ),
        migrations.DeleteModel(
            name='BannerTag',
        )
    ]
