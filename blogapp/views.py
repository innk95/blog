# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

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

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/blogapp/login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "blogapp/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "blogapp/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/blogapp/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

