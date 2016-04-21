if [ ! -e ~/.ssh ] ; then
  mkdir ~/.ssh
  cp id_rsa ~/.ssh/id_rsa
  cp id_rsa.pub ~/.ssh/id_rsa.pub
  chmod 600 ~/.ssh/id_rsa.pub
  chmod 600 ~/.ssh/id_rsa
fi
#eval "$(ssh-agent -s)"
if [ -z "$SSH_AUTH_SOCK" ] ; then
  exec ssh-agent bash -c "ssh-add ; $0"
  exit
fi
# eval "$(ssh-agent)" 
# exec ssh-agent bash
sleep 2
#loook for more complex way to do the same at http://pastebin.com/88rpiTiF
ssh-add ~/.ssh/id_rsa
ssh-add -l  
cd web

