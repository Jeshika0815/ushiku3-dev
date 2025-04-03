# Generated by Django 5.1.5 on 2025-03-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyoshiji', '0006_workorder_planed_value_workorder_work_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='planed_value',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, verbose_name='計画数'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='work_range',
            field=models.CharField(default='例) P1~P27の エ1~エ3 製造票のコピー', max_length=200, verbose_name='作業範囲'),
        ),
    ]
