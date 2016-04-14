# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160223_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerlog',
            name='email_to_report',
            field=models.CharField(default=b'nfc.dev.cita@gmail.com', max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='printer',
            name='emailReport',
            field=models.CharField(default=b'nfc.dev.cita@gmail.com', max_length=40),
        ),
    ]
