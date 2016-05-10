#-*- coding: utf-8 -*-
# 3) В вашем приложении qa  в файле models.py определите следующие модели обладающие следующими полями (названия моделей и полей важны!)

# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"

# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа

from django.db import models
from datetime import datetime  

class Like(models.Model):
    user = models.CharField(max_length=254, default="testuser")
    verbose_name = 'q amd a like user'
    
    def __str__(self):              
      # __unicode__ on Python 2
       
        return self.verbose_name    
    
    class Meta:
        db_table = "like"
        
class Author(models.Model):
    name = models.CharField(max_length=254, default="testauthor")
    verbose_name = 'q amd a author'

    def __str__(self):              # __unicode__ on Python 2
        return self.name
      
class Question(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_at = models.DateField(default=datetime.now, blank=True)
    text = models.TextField(default="", blank=True)
    rating = models.IntegerField(default=0)
    like = models.ManyToManyField(Like, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name      
      
class Tag(models.Model):
    verbose_name = 'q amd a tag'
    name = models.CharField(max_length=128, default="test")
    members = models.ManyToManyField(Question, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
      
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    added_at = models.DateField(default=datetime.now, blank=True)
    text = models.TextField(default="", blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name