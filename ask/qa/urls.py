# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='test'),
]
