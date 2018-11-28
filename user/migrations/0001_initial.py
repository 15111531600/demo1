# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-27 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32, verbose_name='your location')),
                ('min_distance', models.IntegerField(default=1, verbose_name='min distance')),
                ('max_distance', models.IntegerField(default=10, verbose_name='max distance')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='min age')),
                ('max_dating_age', models.IntegerField(default=45, verbose_name='max age')),
                ('dating_sex', models.CharField(choices=[('M', 'man'), ('F', 'woman')], max_length=8, verbose_name='target sex')),
                ('vibration', models.BooleanField(default=True, verbose_name='is not take on vibration')),
                ('only_matche', models.BooleanField(default=False, verbose_name='is not for other')),
                ('auto_play', models.BooleanField(default=False, verbose_name='is not auto play video')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('M', 'man'), ('F', 'woman')], max_length=8)),
                ('birth_year', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_day', models.IntegerField()),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
