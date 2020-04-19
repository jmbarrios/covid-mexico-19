#!/bin/bash
export $(grep -v '^#' /code/covid.env | xargs)
export POSTGRES_HOST='db'

/usr/local/bin/python /code/manage.py actualizar_casos --descargar >> /code/cron.log 2>&1
