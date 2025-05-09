# Generated by Django 5.1.5 on 2025-03-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyoshiji', '0005_workorder_work_trenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='planed_value',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=1, verbose_name='計画数'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='work_group',
            field=models.CharField(default=0, max_length=10, verbose_name='製作グループ'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='work_range',
            field=models.TextField(default=0, verbose_name='作業範囲'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='work_type',
            field=models.CharField(default=0, max_length=2, verbose_name='作業種別'),
        ),
    ]
