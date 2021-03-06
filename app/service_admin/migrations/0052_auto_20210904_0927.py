# Generated by Django 3.2.5 on 2021-09-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0051_auto_20210904_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='colour',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='service_admin.colour'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visualisationfield',
            name='colour',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='service_admin.colour'),
            preserve_default=False,
        ),
    ]
