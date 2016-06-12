
export GPGKEY=80BA91D1
git config user.email "Billi@users.noreply.github.com"
git config user.name "Billi"
git config --global user.signingkey $GPGKEY
git config --global commit.gpgsign true
# git remote set-url --push origin 'git@github.com:$myuser/$myrepo.git'

