# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_printerlog_email_to_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='emailReport',
            field=models.CharField(default=b'nfc.dev.cita@gmail.com;', max_length=450),
        ),
    ]
