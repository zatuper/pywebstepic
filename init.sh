#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo rm -rf /etc/nginx/sites-enabled/default
sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default2                                          
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello.py
# sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

alias ll='ls -ilhao --color=auto'

cd ~/web
git remote set-url --push origin 'git@github.com:zatuper/pywebstepic.git'
source ssh-add ~/.ssh/id_rsa
ssh-add -l  
