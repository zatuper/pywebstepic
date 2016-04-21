# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


from . import views

urlpatterns = [url(r'^blog/', views.home, name='home'),] 