#!/bin/sh

echo "Esperando a la base de datos..."

while ! nc -z $POSTGRES_HOST 5432; do
  sleep 0.1
done

echo "Conexion exitosa"

exec "$@"
