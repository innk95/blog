# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditProfileForm, WritePostForm, WriteEmailForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView
from django.utils import timezone


# Create your views here.

class WriteEmailView(TemplateView):
    template_name = 'blogapp/index.html'

    def get(self, request):
        form = WriteEmailForm()
        latest_post_list = Post.objects.order_by('-post_pub_date')[:10]
        context = {'latest_post_list': latest_post_list, 'form': form}
        return render(request, 'blogapp/index.html', context)

    def post(self, request):
        form = WriteEmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            post.save()
            return redirect('/blogapp/thanks/')


def detail(request, post_id):
    post_list = Post.objects.all()
    post_take = int(post_id)
    context = {'post_take': post_take, 'post_list': post_list}
    return render(request, 'blogapp/post.html', context)


class WritePostView(TemplateView):
    template_name = 'blogapp/write_post.html'

    def get(self, request):
        form = WritePostForm()
        return render (request, self.template_name, {'form' : form})

    def post(self, request):
        form = WritePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            header = form.cleaned_data['header']
            post_text = form.cleaned_data['post_text']
            image_url = form.cleaned_data['image_url']
            post.post_pub_date = timezone.now()
            post.save()
            context = {'form':form, 'header': header, 'post_text': post_text, 'image_url': image_url}
            return redirect('/blogapp/#about')



def post_new(request):
    return render(request, 'blogapp/post_edit.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = RegistrationForm()
        return render(request, 'blogapp/reg_form.html', {'form': form})


def profile(request):
    context = {'user': request.user}
    return render(request, 'blogapp/profile.html', context)


def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/blogapp/profile')

    else:
        form = EditProfileForm(instance=request.user)

        context = {'form': form}
        return render(request, 'blogapp/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/blogapp/profile')

    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'blogapp/change_password.html', context)

def thanks(request):
    return render(request, 'blogapp/thanks.html')

