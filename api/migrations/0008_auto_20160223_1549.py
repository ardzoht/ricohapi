# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160219_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='cutDate',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='printer',
            name='emailReport',
            field=models.CharField(default=b'nfc.dev.cita@gmail.com', max_length=35),
            preserve_default=True,
        ),
    ]
