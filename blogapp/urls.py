from django.conf.urls import url
from . import views

app_name='blogapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^writepost/', views.writepost, name='writepost'),
    url(r'^post/new/', views.post_new, name='post_new'),


]