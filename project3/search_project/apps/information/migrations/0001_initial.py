# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='资讯名')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('read_nums', models.IntegerField(default=0, verbose_name='阅读数')),
                ('u_fav_nums', models.IntegerField(default=0, verbose_name='用户收藏数')),
                ('u_read_nums', models.IntegerField(default=0, verbose_name='用户阅读数')),
                ('url', models.CharField(default='', max_length=200, verbose_name='url')),
                ('info_from', models.CharField(max_length=50, verbose_name='来源')),
                ('tag', models.CharField(default='', max_length=20, verbose_name='标签')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '资讯',
                'verbose_name_plural': '资讯',
            },
        ),
    ]
