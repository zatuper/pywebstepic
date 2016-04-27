from django.db import models


      
class Author(models.Model):
    name = models.CharField(max_length=254, default='testauthor')
    verbose_name = 'q amd a author'

    def __str__(self):              # __unicode__ on Python 2
        return self.name
      
class Question(models.Model):
    name = models.CharField(max_length=254)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name      
      
      
      
      
class Tag(models.Model):
    verbose_name = 'q amd a tag'
    name = models.CharField(max_length=128, default="test")
    members = models.ManyToManyField(
        Question,
        through='Post',
        through_fields=('Tag', 'Question'),)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
      
class Answer(models.Model):
    name = models.CharField(max_length=254)
    body = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Post(models.Model):
    verbose_name = 'qa submited tag'  
    Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    Count = models.BigIntegerField()
     
    
    def __str__(self):              # __unicode__ on Python 2
        return self.verbose_name  