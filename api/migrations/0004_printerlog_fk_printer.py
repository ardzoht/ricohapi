# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151109_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='printerlog',
            name='fk_printer',
            field=models.ForeignKey(default=0, to='api.Printer'),
            preserve_default=False,
        ),
    ]
