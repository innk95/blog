# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_auto_20170809_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myemail',
            name='email',
        ),
    ]
