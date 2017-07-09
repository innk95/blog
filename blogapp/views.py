# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-post_pub_date')[:10]
    output = ','.join([q.header for q in latest_post_list])
    return HttpResponse(output)


def detail (request, header_id):
    return HttpResponse('Ты смотришь запись под номером %s.' % header_id)