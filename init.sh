#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/nginx.conf 
sudo ln  /home/box/web/etc/nginx-main /etc/nginx/nginx.conf 

#sudo rm -rf /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-enabled/default   
sudo rm -f /etc/gunicorn.d/django.example 
sudo rm -f  /etc/gunicorn.d/wsgi.example  
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/test /etc/gunicorn.d/test
# sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

# alias in bashrc
cd ~/web

source keys.sh
source initgit.sh
