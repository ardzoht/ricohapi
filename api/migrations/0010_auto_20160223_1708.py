# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20160223_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='cutDate',
            field=models.IntegerField(default=1),
        ),
    ]
