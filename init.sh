#!/usr/bin/env bash
trap "set +x; sleep 1; set -x" DEBUG
#sudo /usr/bin/apt-get -qy update > /dev/null
#sudo /usr/bin/apt-get -qy dist-upgrade > /dev/null
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
sudo echo 'export WORKON_HOME="$HOME/.virtualenvs"' >> /home/box/.bashrc
sudo echo './usr/local/bin/virtualenvwrapper.sh' >> /home/box/.bashrc
sudo echo 'export alias ls="ls -h --color"' >> /home/box/.bashrc
# The ubiquitous 'll': directories first, with alphanumeric sorting:
sudo alias 'export ll="ls -lv --group-directories-first"1' >> /home/box/.bashrc
sudoalias 'export tree="tree -Csuh"' >> /home/box/.bash_alias    #  Nice alternative to 'recursive ls' ...
#alias lx='ls -lXB'         #  Sort by extension.
#alias lk='ls -lSr'         #  Sort by size, biggest last.
#alias lt='ls -ltr'         #  Sort by date, most recent last.
#alias lc='ls -ltcr'        #  Sort by/show change time,most recent last.
#alias lu='ls -ltur'        #  Sort by/show access time,most recent last.
#alias lm='ll |more'        #  Pipe through 'more'
#alias lr='ll -R'           #  Recursive ls.
#alias la='ll -A'           #  Show hidden files.

source .bashrc
source .bash_alias
cd ~/web
source keys.sh
cd ~/web
bash initgit.sh
