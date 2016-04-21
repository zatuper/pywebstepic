# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template
# Create your views here.
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/
# Выберите правильные способы получения GET параметров в Django view 
# Напишите текст (без переносов строк и пробелов), который получится при шаблонизации index.html - 
# (ответ в контроллере popular)

def view(request):
  # value = request.get('name')
  # value = request['name']
  # value = request.GET('name')
    value = request.GET['name'] # правильно
  # value = request.GET.get('name') #тоже правильно, но еще напишет Not Found: /favicon.ico 
    return  HttpResponse(value)

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
    template = get_template('index.html')
    html = template.render({'name': 'hello World'})  
    return HttpResponse(html)
def new(request):
    return HttpResponse('OK')
  
