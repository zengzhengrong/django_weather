# Generated by Django 2.1.7 on 2019-02-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20190218_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_cn',
            field=models.BooleanField(default=False, verbose_name='China weather'),
        ),
    ]
