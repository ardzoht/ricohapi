# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160223_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='cutDate',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
