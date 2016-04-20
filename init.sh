#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
#sudo /usr/bin/apt-get -qy update > /dev/null
#sudo /usr/bin/apt-get -qy dist-upgrade > /dev/null
## may be useful # sudo pip install -upgrade gunicorn > /dev/null
     # pip install -upgrade gunicorn > /dev/null

#delete unwanted default configs
sudo rm -f /etc/nginx/nginx.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/gunicorn.d/django.example
sudo rm -f /etc/gunicorn.d/wsgi.example
sudo rm -f /etc/gunicorn.d/test

#rock our custom configs  to work
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/box/web/etc/nginx-main /etc/nginx/nginx.conf
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test

sudo /etc/init.d/nginx restart
# sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

#  load keys
cd ~/web
cd ~

source .bash_alias
cd ~/web
source keys.sh
cd ~/web
bash initgit.sh
