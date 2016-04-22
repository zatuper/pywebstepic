python -c "import django;print (django.get_version())" #какая версия? 
python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)" # где установлен?
sudo pip install --upgrade django  

