# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
from .models import UserProfile
from .models import MyEmail

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(MyEmail)

