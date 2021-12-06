# Generated by Django 3.2.5 on 2021-09-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0056_auto_20210905_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabulationMetric',
            fields=[
                ('tabmetric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_admin.tabmetric')),
            ],
            options={
                'db_table': 'cms"."tabulation_metric',
            },
            bases=('service_admin.tabmetric',),
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.tabulation_metric')"
        ),
        migrations.CreateModel(
            name='VisualisationMetric',
            fields=[
                ('tabmetric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_admin.tabmetric')),
            ],
            options={
                'db_table': 'cms"."visualisation_metric',
            },
            bases=('service_admin.tabmetric',),
        ),
        migrations.RunSQL(
            "SELECT create_reference_table('cms.visualisation_metric')"
        ),
        migrations.RemoveField(
            model_name='tabulationfield',
            name='metrics',
        ),
        migrations.RemoveField(
            model_name='visualisationfield',
            name='metrics',
        ),
        migrations.AlterField(
            model_name='tabmetric',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabmetric_related_colours', to='service_admin.colour'),
        ),
        migrations.AlterField(
            model_name='tabmetric',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabmetric_related_tabs', to='service_admin.metricreference', to_field='metric'),
        ),
        migrations.AddField(
            model_name='visualisationmetric',
            name='visualisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visualisationmetric_related', to='service_admin.visualisationfield'),
        ),
        migrations.AddField(
            model_name='tabulationmetric',
            name='tabulation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tabulationmetric_related', to='service_admin.tabulationfield'),
        ),
    ]