# Generated by Django 5.1.5 on 2025-03-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyodenpyo', '0003_alter_worklog_work_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='worklog',
            name='work_minute',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='分'),
        ),
        migrations.AddField(
            model_name='worklog',
            name='work_trenum',
            field=models.CharField(default=0, max_length=3, verbose_name='枝番'),
        ),
        migrations.AlterField(
            model_name='worklog',
            name='work_hours',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4, verbose_name='時間'),
        ),
        migrations.AlterField(
            model_name='worklog',
            name='work_number',
            field=models.CharField(max_length=4, verbose_name='工番'),
        ),
    ]
