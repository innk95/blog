# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myemail',
            name='name',
            field=models.EmailField(max_length=50),
        ),
    ]
