# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20170709_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='static/blogapp/downloads/default.png', max_length=200),
        ),
    ]
