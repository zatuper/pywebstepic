# -*- coding: utf-8 -*-
# то что из задания относится к views.py:
# 2) Создайте view для обработки следующих страниц
# URL = /?page=2
# Главная страница. Список "новых" вопросов. Т.е. последний заданный вопрос - первый в списке. 
# На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page.  
# На страницу выводится по 10 вопросов. В списке вопросов должны выводится заголовки (title) вопросов 
# и ссылки на страницы отдельных вопросов.
# URL = /popular/?page=3
# Cписок "популярных" вопросов. Сортировка по убыванию поля rating. На этой странице 
# должна работать пагинация. Номер страницы указывается в GET параметре page.  На страницу выводится 
# по 10 вопросов. В списке вопросов должны выводится заголовки (title) вопросов и ссылки на страницы 
# отдельных вопросов.
# URL = /question/5/
# Страница одного вопроса. На этой странице должны выводится заголовок 
# (title), текст (text) вопроса и все ответы на данный вопрос, без пагинации. 
# В случае неправильного id вопроса view должна возвращать 404.
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import Http404
from django.template.loader import get_template
from django.template import RequestContext
from .models import Author, Question, Like, Tag

def question(request, question_id):
    
    try:
        question = Question.objects.get(id=int(question_id))
        print question.author 
        question_author=question.author
        print question
        print question.text
        question_text=question.text
        print question_id
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    template = get_template('question.html')
    html = template.render({'question':question,  'question_id':question_id, 'question_author':question_author, 'question_text':question_text })
    return HttpResponse(html)
       

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
def popular(request, question_id=3):
   
    try:
        question = Question.objects.get(id=int(question_id))
        print question_id
        print question
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    template = get_template('index.html')    
    html = template.render({'question': question})  
    return HttpResponse(html)
def new(request):
    return HttpResponse('OK')
  
  
  
