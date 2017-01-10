#!/bin/bash
set -e
DJANGO_DIR={{ django_dir }}
PROJECT_DIR={{ project_dir }}
LOGFILE=$PROJECT_DIR/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3

cd {{ django_dir }}
source $PROJECT_DIR/venv/bin/activate
export DATABASE_URL='postgres://{{ db_user }}:{{ db_password }}@localhost/{{ db_name }}'
export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH

test -d $LOGDIR || mkdir -p $LOGDIR
exec $PROJECT_DIR/venv/bin/gunicorn bookshop.wsgi:application -w $NUM_WORKERS \
  --log-level=info --log-file=$LOGFILE -b 0.0.0.0:9000 2>>$LOGFILE
