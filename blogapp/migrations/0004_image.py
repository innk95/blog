# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20170708_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doument', models.FileField(upload_to='downloads/')),
            ],
        ),
    ]
