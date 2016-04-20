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
    url(r'^login/', view.login, name='login'),
    url(r'^signup/', view.signup, name='signup'),
    url(r'^ask/', view.ask, name='ask'),
    url(r'^popular/', view.popular, name='popular'),
    url(r'^new/', view.new, name='new'),
    url(r'^$',     include('qa.urls')),
    url(r'^question/([0-9]{4})/$', include('qa.urls')),
    url(r'^blog/', include('blog.urls')),
 
]