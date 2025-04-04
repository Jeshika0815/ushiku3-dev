# Generated by Django 5.1.5 on 2025-03-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyoshiji', '0010_alter_workorder_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='buy_check',
            field=models.CharField(default='2025/3/13 吉川 将暉', max_length=30, verbose_name='購買確認'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='publish_check',
            field=models.CharField(default='2025/3/11 吉川 将暉', max_length=30, verbose_name='作成'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='recive_check',
            field=models.CharField(default='2025/3/14 吉川 将暉', max_length=30, verbose_name='受け取り確認'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='syounin_check',
            field=models.CharField(default='2025/3/10 吉川 将暉', max_length=30, verbose_name='承認'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='workset_check',
            field=models.CharField(default='2025/3/12 吉川 将暉', max_length=30, verbose_name='工数設定'),
        ),
    ]
