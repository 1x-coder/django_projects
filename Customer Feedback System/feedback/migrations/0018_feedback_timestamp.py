# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 05:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0017_auto_20170826_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 3, 8, 29, 15, 581565)),
        ),
    ]