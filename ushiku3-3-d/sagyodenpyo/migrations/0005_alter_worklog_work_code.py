# Generated by Django 5.1.5 on 2025-03-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagyodenpyo', '0004_worklog_work_minute_worklog_work_trenum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='work_code',
            field=models.CharField(choices=[('001', 'P001'), ('002', 'P002'), ('003', 'P003'), ('004', 'P004'), ('005', 'P005'), ('006', 'P006'), ('007', 'P007'), ('008', 'P008'), ('009', 'P009'), ('010', 'P010'), ('011', 'P011'), ('012', 'P012'), ('013', 'P013'), ('014', 'P014'), ('015', 'P015'), ('016', 'P016'), ('017', 'P017'), ('018', 'P018'), ('019', 'P019'), ('402', 'P402'), ('602', 'P602'), ('701', 'P701'), ('903', 'P903'), ('908', 'P908'), ('909', 'P909'), ('999', 'P999')], max_length=3, verbose_name='作業コード'),
        ),
    ]
