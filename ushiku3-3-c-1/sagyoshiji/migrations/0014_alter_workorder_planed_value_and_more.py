# Generated by Django 5.1.7 on 2025-04-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyoshiji', '0013_alter_workorderprogress_achievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='planed_value',
            field=models.DecimalField(decimal_places=0, default='', max_digits=3, verbose_name='計画数'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='process_pattern',
            field=models.CharField(choices=[('1', 'No.1'), ('2', 'No.2'), ('3', 'No.3'), ('4', 'No.4'), ('5', '一般工程'), ('6', 'その他')], max_length=10, verbose_name='製造工程パタン'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='work_group',
            field=models.CharField(choices=[('1', '牛久工場'), ('2', '千葉工場'), ('3', '石下工場'), ('4', 'その他')], default=0, max_length=10, verbose_name='製作グループ'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='work_range',
            field=models.CharField(default='P0〜0 .工0~0', max_length=200, verbose_name='作業範囲'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='work_trenum',
            field=models.CharField(default='', max_length=3, verbose_name='枝番'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='work_type',
            field=models.CharField(choices=[('1', 'FB'), ('2', 'PL')], default=0, max_length=2, verbose_name='FB・PL'),
        ),
    ]
