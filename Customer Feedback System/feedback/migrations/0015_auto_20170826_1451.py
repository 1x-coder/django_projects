# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_auto_20170826_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_pic',
            field=models.ImageField(default='/pic_folder/nologo.jpg', upload_to='pic_folder/'),
        ),
    ]
