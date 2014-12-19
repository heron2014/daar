from django.conf.urls import patterns, include, url
from profiles import views

urlpatterns = patterns('',
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<username>\w+)/$', views.single_user, name='single_user'),


)
