FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -yq cron wget nano gdal-bin binutils libproj-dev libgdal-dev memcached libmemcached-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
RUN mkdir /code/staticfiles
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY docker/cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN touch /var/log/cron.log

COPY docker/iniciar.sh /code/docker/iniciar.sh
RUN chmod +x /code/docker/iniciar.sh

COPY . /code/

ENTRYPOINT ["/code/docker/iniciar.sh"]
