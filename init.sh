sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
git config user.email "s@s.r"
git config user.name "s@s.r"
alias ll='ls -ilhao --color=auto'
mkdir ~/.ssh
cp id_rsa ~/.ssh/id_rsa
cp id_rsa.pub ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa
# eval "$(ssh-agent -s)"
eval "$(ssh-agent)" 
exec ssh-agent bash
sleep 2
ssh-add ~/.ssh/id_rsa
#loook for more complex way to do the same at http://pastebin.com/88rpiTiF
cd ~/web
git remote set-url --push origin 'git@github.com:zatuper/pywebstepic.git'                 
                                                                                                                    
                                   
