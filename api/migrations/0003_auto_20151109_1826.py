# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151105_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrinterLog',
            fields=[
                ('log_id', models.IntegerField(serialize=False, primary_key=True)),
                ('global_counter', models.IntegerField()),
                ('counter_print_bw', models.IntegerField()),
                ('counter_print_color', models.IntegerField()),
                ('counter_copy_bw', models.IntegerField()),
                ('counter_copy_color', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='printer',
            name='counter_copy_bw',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='counter_copy_color',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='counter_print_bw',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='counter_print_color',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='global_counter',
        ),
        migrations.AddField(
            model_name='printer',
            name='description',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
