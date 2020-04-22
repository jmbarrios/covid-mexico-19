FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -yq cron wget netcat nano gdal-bin binutils libproj-dev libgdal-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY docker/cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN touch /var/log/cron.log

COPY docker/esperar.sh /code/esperar.sh
COPY docker/iniciar.sh /code/iniciar.sh
COPY docker/actualizar.sh /code/actualizar.sh
COPY manage.py /code/manage.py

COPY covid_api/ /code/covid_api/
COPY covid_data/ /code/covid_data/
COPY covid_mapa/ /code/covid_mapa/
COPY covid_update/ /code/covid_update/
COPY covid_datos_adicionales/ /code/covid_datos_adicionales/
COPY django_covid/ /code/django_covid/

RUN mkdir /code/datos

ENTRYPOINT ["/code/esperar.sh"]
