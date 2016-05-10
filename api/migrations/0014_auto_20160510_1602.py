# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20160419_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='printers',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='printer',
            name='client',
            field=models.CharField(default=b'CITA', max_length=30),
            preserve_default=True,
        ),
    ]
