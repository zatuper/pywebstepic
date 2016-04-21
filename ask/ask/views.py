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
def login(request, *args, **kwargs):
  # id = args['id'] # это неправильно синтаксичечки
    id = kwargs['id'] # это правильно
  # id = request.arggs # неправильно, это другой способ можно написать 
    resp = 'OK ' + str(id)
    return HttpResponse(resp)
def signup(request):
    return HttpResponse('OK')
def ask(request):
    return HttpResponse('OK')
def popular(request):
    return HttpResponse('OK')
def new(request):
    return HttpResponse('OK')
  
