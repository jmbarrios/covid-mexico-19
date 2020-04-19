#!/bin/bash
set

python docker/esperar.py
python manage.py flush --no-input
python manage.py migrate
python manage.py actualizar_catalogos --descargar
python manage.py actualizar_casos --descargar
cron
