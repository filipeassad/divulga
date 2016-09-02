# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-02 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video_canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(auto_created=True)),
                ('titulo', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='video_site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(auto_created=True)),
                ('titulo', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=500)),
                ('link_gif', models.CharField(max_length=500)),
            ],
        ),
    ]
