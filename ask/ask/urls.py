# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/



urlpatterns = [
    url(r'^login/(?P<id>\d+)/?', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.new, name='new'),
    url(r'^view/', views.view, name='view'),  
    url(r'^$',     include('qa.urls')),
    url(r'^question/([0-9]{3})/$', include('qa.urls')),
    url(r'^question/(\d+)/$', include('qa.urls')),
    url(r'^blog/', include('blog.urls')),
 
]
