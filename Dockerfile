FROM postgres:10-alpine
FROM python:3.7

ENV DEBIAN_FRONTEND=noninteractive
ENV PGDATA=/pgdata

RUN apt-get update \
  && apt-get install -yq cron wget nano postgis\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

COPY cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN touch /var/log/cron.log
   

ENTRYPOINT ["/bin/bash"]
