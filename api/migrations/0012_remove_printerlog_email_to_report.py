# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160224_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printerlog',
            name='email_to_report',
        ),
    ]
