from django.shortcuts import render

# blog
def home(request):
    return HttpResponse('Hello World')
