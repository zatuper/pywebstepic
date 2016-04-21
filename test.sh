cd ask;
gunicorn -b '0.0.0.0:8000' --log-level=debug --error-logfile /home/box/web/log/error-gunicorn.log  --access-logfile /home/box/web/log/access-gunicorn.log --env DJANGO_SETTINGS_MODULE=ask.settings ask.wsgi& 
