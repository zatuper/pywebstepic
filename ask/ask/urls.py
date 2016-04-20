# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^login/', view.login, name='login'),
    url(r'^signup/', view.login, name='signup'),
    url(r'^ask/', view.login, name='ask'),
    url(r'^popular/', view.login, name='popular'),    
    url(r'^$',     include('qa.urls')),
    url(r'^question/([0-9]{4})/$', include('qa.urls')),
    url(r'^blog/', include('blog.urls')),
 
]