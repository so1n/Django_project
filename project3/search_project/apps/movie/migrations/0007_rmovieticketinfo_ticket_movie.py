# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20180331_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmovieticketinfo',
            name='ticket_movie',
            field=models.CharField(default='', max_length=50, verbose_name='电影名'),
        ),
    ]
