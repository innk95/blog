# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='User', null=True)
    header = models.CharField(max_length=200)
    post_text = models.CharField(max_length=1000)
    post_pub_date = models.DateTimeField('date published')
    image_url = models.CharField(max_length=200, default='/static/blogapp/downloads/default.png')


class Comment(models.Model):
    comment_text = models.CharField(max_length=50)
    comment_pub_date = models.DateTimeField('date comment published')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class MyEmail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)


