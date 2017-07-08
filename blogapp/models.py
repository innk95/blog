# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=20)
    post_text = models.CharField(max_length=300)
    post_pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    comment_text = models.CharField(max_length=50)
    comment_pub_date = models.DateTimeField('date comment published')
