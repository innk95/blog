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
    post_list = Post.objects.all()
    post_take = int(post_id)
    context = {'post_take' : post_take, 'post_list' : post_list}
    return render(request, 'blogapp/post.html', context)

def writepost (request):
    return render(request, 'blogapp/write_post.html')

def post_new(request):
    return render(request, 'blogapp/post_edit.html')

def sign_up (request):
    return render(request, 'blogapp/sign_up.html')





