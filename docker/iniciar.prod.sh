#!/bin/bash
set
python docker/esperar.py
python manage.py migrate
python manage.py actualizar_catalogos --descargar
python manage.py actualizar_casos --descargar
python manage.py collectstatic --no-input --clear
cron

exec "$@"
