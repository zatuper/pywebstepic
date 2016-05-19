#-*- coding: utf-8 -*-
# сохраните все введенные команды в отдельном файле, что бы потом вы могли легко их повторить.

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

# В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.

# 4) С помощью команды manage.py /syncdb  создайте необходимые таблицы для ваших моделей -- в django  версии > 1.6 migrate
# 5) Не забудьте закомитить и сохранить на github созданные файлы.

from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # вместо __unicode__ on Python 2 используется декоратор python_2_unicode_compatible
class Like(models.Model):
    user = models.CharField(max_length=254, default="testuser")
    verbose_name = 'q amd a like user'
    
    def __str__(self):              
             
        return self.verbose_name    
    
    class Meta:
        db_table = "like"
        
@python_2_unicode_compatible        
class Author(models.Model):
    name = models.CharField(max_length=254, default="testauthor")
    verbose_name = 'q amd a author is '

    def __str__(self):     
        return self.name
      
@python_2_unicode_compatible      
class Question(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_at = models.DateField(default=timezone.now, blank=True)
    text = models.TextField(default="", blank=True)
    rating = models.IntegerField(default=0)
    like = models.ManyToManyField(Like, blank=True)
     
    
    def __str__(self):       
        return self.title     
    def get_absolute_url(self):                          # 7
        return '/question/%d/' % self.pk                 # 8
      
@python_2_unicode_compatible      
class Tag(models.Model):
    verbose_name = 'q amd a tag'
    name = models.CharField(max_length=128, default="test")
    members = models.ManyToManyField(Question, blank=True)
    
    def __str__(self):       
        return self.name
      
@python_2_unicode_compatible      
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    added_at = models.DateField(default=timezone.now, blank=True)
    text = models.TextField(default="", blank=True)

    def __str__(self):       
        return self.name