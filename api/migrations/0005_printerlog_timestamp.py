# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_printerlog_fk_printer'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 10, 19, 17, 22, 10623, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
