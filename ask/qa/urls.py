#/
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # url(r'^$', 'handler404')
    url(r'^404/$', 'django.views.defaults.page_not_found')
    url(r'^articles/(?P<ID_qa>\d{6})/$', 'qa.views.quest'),
    
)
