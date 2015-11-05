# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('printer_id', models.IntegerField(serialize=False, primary_key=True)),
                ('global_counter', models.IntegerField()),
                ('counter_print_bw', models.IntegerField()),
                ('counter_print_color', models.IntegerField()),
                ('counter_copy_bw', models.IntegerField()),
                ('counter_copy_color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=40)),
                ('user_global_counter', models.IntegerField()),
                ('user_counter_print_bw', models.IntegerField()),
                ('user_counter_print_color', models.IntegerField()),
                ('user_counter_copy_bw', models.IntegerField()),
                ('user_counter_copy_color', models.IntegerField()),
                ('printers', models.ManyToManyField(to='api.Printer')),
            ],
        ),
    ]
