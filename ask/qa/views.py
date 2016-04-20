# ask/qa
from django.shortcuts import render
from django.utils.html import escape

# Create your views here.
from django.http import HttpResponse 

def test (request, *args, **kwargs):
    return HttpResponse(escape(repr(request)))
 
def quest (request, *args, **kwargs):
    return HttpResponse('QUEST IS OK')