FROM ubuntu:bionic
ENV DEBIAN_FRONTEND=noninteractive
ENV PGDATA=/pgdata

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US.UTF-8


RUN apt-get update \
  && apt-get install -yq cron wget python3 python3-pip nano postgresql-10 postgresql-server-dev-10 postgis\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/

COPY cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN touch /var/log/cron.log
   

ENTRYPOINT ["/bin/bash"]
