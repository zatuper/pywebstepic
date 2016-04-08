#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo rm -rf /etc/nginx/sites-enabled/default
sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default2                                          
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

# alias in bashrc
cd ~/web

source keys.sh
source initgit.sh
