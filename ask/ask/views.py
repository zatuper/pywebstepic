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
    return HttpResponse('OK')
def signup(request):
    return HttpResponse('OK')
def ask(request):
    return HttpResponse('OK')
def popular(request):
    return HttpResponse('OK')
def new(request):
    return HttpResponse('OK')
  
