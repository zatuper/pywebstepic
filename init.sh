#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln  /home/box/web/etc/nginx-main /etc/nginx/nginx.conf 

#sudo rm -rf /etc/nginx/sites-enabled/default
sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default2   
sudo mv /etc/gunicorn.d/django.example  /home/box/web/etc/django.example
sudo mv /etc/gunicorn.d/wsgi.example  /home/box/web/etc/wsgi.example
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/test /etc/gunicorn.d/test
# sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

# alias in bashrc
cd ~/web

source keys.sh
source initgit.sh
