# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-post_pub_date')[:10]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blogapp/index.html', context)


def detail (request, post_id):
    return HttpResponse('Ты смотришь запись под номером %s.' % post_id)


