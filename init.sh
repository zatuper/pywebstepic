sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
git config user.email "s@s.r"
git config user.name "s@s.r"
alias ll='ls -ilhao --color=auto' 
eval "$(ssh-agent -s)"
eval "$(ssh-agent)"   
ssh-add /home/box/.ssh/id_rsa
#loook at http://pastebin.com/88rpiTiF
