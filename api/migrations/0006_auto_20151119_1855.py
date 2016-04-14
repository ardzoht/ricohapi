# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_printerlog_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerlog',
            name='counter_bw_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_color_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='printer',
            name='printer_id',
            field=models.CharField(max_length=25, serialize=False, primary_key=True),
        ),
    ]
