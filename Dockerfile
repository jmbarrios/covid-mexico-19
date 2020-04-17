FROM ubuntu:bionic
ENV DEBIAN_FRONTEND=noninteractive
ENV PGDATA=/pgdata
RUN apt-get update \
  && apt-get install -yq wget python3 python3-pip nano postgresql-10 postgresql-server-dev-10 postgis\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/


#RUN chown postgres /var/lib/postgresql/10/main
#RUN chgrp postgres /var/lib/postgresql/10/main 
#RUN chmod -R 0700 /var/lib/postgresql/10/
#RUN su postgres
#RUN /var/lib/postgresql/10/bin/initdb -D /var/lib/postgresql/10/main/
#RUN exit
#RUN service postgresql start
#RUN su postgres
#RUN psql -c "CREATE DATABASE covid WITH TEMPLATE template0"
#RUN psql -c "CREATE USER covid WITH PASSWORD 'covid'"
#RUN psql -c "GRANT ALL PRIVILEGES ON DATABASE covid TO covid"
#RUN psql -d covid "CREATE EXTENSION postgis"
#RUN exit

#WORKDIR /code
#RUN python3 manage.py migrate
#RUN pyhohn3 manage.py actualizar_catalogos
#RUN python3 manage.py actualizar_casos 


ENTRYPOINT ["/bin/bash"]

