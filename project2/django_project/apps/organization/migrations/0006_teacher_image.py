# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20180211_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%y/%m', verbose_name='头像'),
        ),
    ]
