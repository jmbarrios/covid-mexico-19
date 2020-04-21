FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
<<<<<<< HEAD
  && apt-get install -yq cron wget nc nano gdal-bin binutils libproj-dev libgdal-dev \
=======
  && apt-get install -yq cron wget nano gdal-bin binutils libproj-dev libgdal-dev memcached libmemcached-tools \
>>>>>>> master
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

COPY covid_api/ covid_data/ covid_mapa/ covid_update/ django_covid/ /code/

ENTRYPOINT ["/code/esperar.sh"]
