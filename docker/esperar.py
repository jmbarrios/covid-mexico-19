import time
import os
import psycopg2


port = int(os.environ.get("DB_PORT", 5432))
dbname = os.environ["POSTGRES_DBNAME"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]


while True:
    try:
        psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        break
    except Exception as ex:
        time.sleep(0.1)


print('Conexion exitosa')
