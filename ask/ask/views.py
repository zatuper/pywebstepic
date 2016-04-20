# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/

def home(request):
    return HttpResponse('Hello World')
def login(request):
    return HttpResponse('')
def signup(request):
    return HttpResponse('')
def ask(request):
    return HttpResponse('')
def popular(request):
    return HttpResponse('')
def new(request):
    return HttpResponse('')
  
