from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name='blogapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^writepost/', views.writepost, name='writepost'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^login/$', login, {'template_name' : 'blogapp/login.html'}),
    url(r'^logout/$', logout, {'template_name' : 'blogapp/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile/change-password/$', views.change_password, name='change_password'),

]