cd ask;
gunicorn -b '0.0.0.0:8000' --env DJANGO_SETTINGS_MODULE=ask.settings ask.wsgi& 
