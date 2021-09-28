# Generated by Django 3.2.5 on 2021-09-06 09:59

from django.db import migrations, models
import django.db.models.deletion
from django.db import migrations, models
import service_admin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('service_admin', '0060_auto_20210906_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageURI',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page_name', service_admin.models.fields.VarCharField(max_length=100)),
                ('display_uri', models.URLField(help_text='Relative URI to the page', verbose_name='URL')),
            ],
            options={
                'verbose_name': 'yellow banner',
                'db_table': 'covid19"."page_uri',
            },
        ),
        migrations.DeleteModel(
            name='PageURI',
        ),
        migrations.RemoveField(
            model_name='tabmetric',
            name='tab',
        ),
        # migrations.AlterField(
        #     model_name='oversightrecord',
        #     name='id',
        #     field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        # ),
        # migrations.AlterField(
        #     model_name='service',
        #     name='id',
        #     field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        # ),
        migrations.AlterField(
            model_name='tabfield',
            name='field_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ['visualisationfield', 'tabulationfield']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='tabmetric',
            name='field_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ['visualisationfield', 'tabulationfield']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.DeleteModel(
            name='BannerPage',
        ),
    ]
