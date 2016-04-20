from django.shortcuts import render

# ask
def home(request):
    return HttpResponse('Hello World')