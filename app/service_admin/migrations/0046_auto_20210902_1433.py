# Generated by Django 3.2.5 on 2021-09-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_admin', '0045_auto_20210902_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabulationfield',
            name='value',
        ),
        migrations.RemoveField(
            model_name='visualisationfield',
            name='value',
        ),
        migrations.AlterField(
            model_name='visualisationfield',
            name='nested_metrics',
            field=models.JSONField(default=dict, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='visualisationfield',
            name='parameter',
            field=models.CharField(help_text='Attribute name for the 3rd dimension.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='visualisationfield',
            name='type',
            field=models.CharField(choices=[('line', 'Line'), ('bar', 'Bar'), ('heatmap', 'Heatmap')], max_length=10, null=True),
        ),
    ]
