#/
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/
# url(r'^$', 'handler404')

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^question/(?P<ID_qa>\d{6})/$', 'qa.views.quest'),
    
)
