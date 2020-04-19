python docker/esperar.py
python manage.py migrate
python manage.py actualizar_catalogos --descargar
python manage.py actualizar_casos --descargar
cron
gunicorn django_covid.wsgi:application --bind 0.0.0.0:8000 -w 4
