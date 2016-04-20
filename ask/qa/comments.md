# задача на urls.py - вернуть OK только для /question/<123 произольно>/
#/
#/login/
#/signup/
#/question/<123>/    # вместо <123> - произвольный ID
#/ask/
#/popular/
#/new/
# url(r'^$', 'handler404')
# url(r'^404/$', 'django.views.defaults.page_not_found'),
# r'^question/(?P<ID_qa>\d{6})/$'

Django version 1.9.5, using settings 'ask.settings'                                                                                            
Starting development server at http://0.0.0.0:8000/ 
 gunicorn --env DJANGO_SETTINGS_MODULE=myproject.settings myproject.wsgi