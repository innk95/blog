# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20170709_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(default='static/downloads/default.jpg', upload_to='static/downloads/'),
        ),
    ]