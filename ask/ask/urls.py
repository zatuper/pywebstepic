# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$',     include('qa.urls')),
    url(r'^question/([0-9]{4})/$', include('qa.urls')),
    url(r'^blog/', include('blog.urls')),
 
]