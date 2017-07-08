# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Стартовая страница')

def detail (request, header_id):
    return HttpResponse('Ты смотришь запись под номером %s.' % header_id)