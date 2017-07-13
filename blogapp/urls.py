from django.conf.urls import url
from . import views

app_name='blogapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^writepost/', views.writepost, name='writepost'),
    url(r'^post/new/', views.post_new, name='post_new'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),




]