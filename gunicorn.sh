#!/bin/bash
NAME=ask                              #Name of the application (*)
DJANGODIR=/home/box/web/ask/ask             # Django project directory (*)
# SOCKFILE=/var/www/test/run/gunicorn.sock        # NO ! we not will communicate using this unix socket (*)
  USER=box                                        # the user to run as (*)
# GROUP=box                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=/home/box/web/ask/ask/settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=/home/box/web/ask/ask/wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
#source /var/www/test/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
# as no virtualnv no need of /var/www/test/venv/bin/
exec gunicorn ${DJANGO_WSGI_MODULE}:application --name $NAME --workers $NUM_WORKERS --user $USER --bind='0.0.0.0:8000'
#no socket unix:$SOCKFILE
#
