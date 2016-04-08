mkdir ~/.ssh
cp id_rsa ~/.ssh/id_rsa
cp id_rsa.pub ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa
source eval "$(ssh-agent -s)"
# eval "$(ssh-agent)" 
# exec ssh-agent bash
sleep 2
#loook for more complex way to do the same at http://pastebin.com/88rpiTiF
source ssh-add ~/.ssh/id_rsa
ssh-add -l  
