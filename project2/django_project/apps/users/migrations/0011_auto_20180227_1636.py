# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180227_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(1997, 1, 1), null=True, verbose_name='生日'),
        ),
    ]
