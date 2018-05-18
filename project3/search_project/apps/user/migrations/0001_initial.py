# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 23:30
from __future__ import unicode_literals

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=6, verbose_name='性别')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('user_image', models.ImageField(default='static/image/user/default.png', upload_to='static/image/user/%Y/%m', verbose_name='用户头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'abstract': False,
                'verbose_name': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], max_length=30, verbose_name='发送类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name_plural': '邮箱验证码',
                'verbose_name': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='HousePush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_address', models.CharField(max_length=50, verbose_name='地址')),
                ('house_price', models.CharField(max_length=20, verbose_name='价格')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
            ],
            options={
                'verbose_name_plural': '用户house表单',
                'abstract': False,
                'verbose_name': '用户house表单',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '标签',
                'abstract': False,
                'verbose_name': '标签',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.CharField(max_length=50, verbose_name='收藏的id')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('type', models.CharField(choices=[('house', '房源'), ('movie', '电影'), ('information', '资讯')], default='房源', max_length=6, verbose_name='类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户与收藏',
                'abstract': False,
                'verbose_name': '用户与收藏',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_tag',
            field=models.ManyToManyField(to='user.Tag', verbose_name='用户标签'),
        ),
    ]
