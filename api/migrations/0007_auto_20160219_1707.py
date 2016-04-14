# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151119_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerlog',
            name='counter_fax_bw',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_fax_color',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_toner_black',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_toner_cyan',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_toner_magenta',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printerlog',
            name='counter_toner_yellow',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
