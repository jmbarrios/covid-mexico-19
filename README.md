# covid-mexico-19
Servicio API REST para la consulta de casos COVID-19 en México.

Este repositorio mantiene el código para generar un servicio API REST para la consulta de datos COVID-19 en México.
El servicio fue construido utilizando python como lenguaje principal; se emplearon django y django-rest-framework
para facilitar el manejo de la información y la construcción del servicio REST.

# Fuentes de la información

## Casos COVID

Los datos de casos son tomados directamente de la plataforma gubernamental

  [https://www.gob.mx/salud/documentos/datos-abiertos-152127](https://www.gob.mx/salud/documentos/datos-abiertos-152127)

El servicio intenta actualizarse cada día (con una frecuencia de intentos de 2 horas). Dado que no deseamos
modificar en modo alguno los datos provistos por la Secretaría de Salud, en cada actualización
la tabla de casos es borrada por completo y reemplazada por la nueva.

## Municipios y Entidades

Los códigos, las claves y los polígonos que definen a cada entidad y municipio fueron tomadas del
marco geoestadístico (versión diciembre 2018) publicado por INEGI en la siguiente liga:

  [https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658](https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658)

Para facilitar su presentación en mapas web las geometrías fueron reproyectadas a EPSG:4326.

## Datos poblacionales

La información de conteos poblacionales por municipio fueron tomadas de las proyecciones
de CONAPO e INEGI para el 2020. La información de población por entidad fue calculada
a partir de los datos municipales.

# Estructura del código

El código está dividido en diversas "aplicaciones" de django.

1. covid_data: En esta aplicación se define el modelo de datos.

2. covid_update: Esta aplicación contiene utilidades y comandos para la actualización de
la información de los casos COVID y catálogos de datos asociados.

3. covid_datos_adicionales: Esta aplicación define modelos de datos para información adicional a nivel municipal
o entidad, como población.

4. covid_api: Esta aplicación define el comportamiento del REST API.

## covid_data

Para la definición del modelo de datos, nos apegamos lo más posible a la estructura de datos publicada por la
Secretaría de Salud.

Hay un modelo de `Caso` que contiene un campo para cada columna de la tabla de casos publicada. Además de una
tabla para los casos, se define un modelo para cada catálogo contenido en el diccionario de
datos publicado. Esto es:

* Resultado
* Nacionalidad
* Origen
* Sector
* Sexo
* SiNo
* TipoPaciente
* Municipio
* Entidad

Se añadió una tabla de países para referenciar el país de nacionalidad y de origen.

* Pais

En los modelos de Entidad y Municipio se añadieron campos para almacenar sus geometrías.

## covid_update

El la actualización de información ocurre en dos estapas:

1. La descarga de la información
2. La carga a la base de datos de la información descargada.

Las funciones de descarga de la información se encuentran en `covid_update/descarga.py`.
Los catálogos requieren un procesamiento muy básico, que consiste en generar un csv
independiente para cada catálogo (`covid_update/catalogos.py`).

El código de actualización de casos y catalogos se puede consultar en
`covid_update/actualizar/casos.py` y `covid_update/actualizar/catalogos.py`,
respectivamente. Al finalizar una actualización de los casos la acción se
registra en la base de datos, junto con información de

1. Fecha y tiempo de actualización
2. Archivo csv utilizado para la actualización
3. Ruta a un archivo .log que contiene mensajes de eventos inesperados en
la actualización de casos.

Para facilitar la ejecución de las actualizaciones incluímos un par de comandos,
definidos en `covid_update/management/commands`. Esto permite correr desde la terminal

    python manage.py actualizar_catalogos --descargar

para descargar y actualizar los catálogos. Y

    python manage.py actualizar_casos --descargar

para descargar y actualizar los casos.

La carpeta de migraciones contiene dos migraciones de datos que ingresan la información
concerniente a las geometrías de las entidades y municipios. Las geometrías son
cargadas de los archivos shape contenidos en la carpeta 
`covid_update/data/marco_geoestadístico`. La última migración concierne la carga
de paises a la base de datos.

## covid_datos_adicionales

Esta aplicación define modelos de datos que relacionan entidades y municipios con
información adicional relevante para el estudio de COVID-19 en méxico.

Por el momento sólo hemos incluído datos relacionados al conteo poblacional de los
municipios y entidades. El modelo de datos se apega a la nomenclatura de INEGI para
los campos de información poblacional. Así el campo 'pf2529' se refiere a la población
femenina entre 25 y 29 años de edad, y el campo 'ppm65ym' se refiere al porcentaje
de la población másculina de 65 años y más de edad.

Esperamos poder añadir otras fuentes de información que sean de utilidad para el
análisis de los datos de COVID-19.

## covid_api

Para la construcción del API REST se utilizó el framework 
['django-rest-framework'](https://www.django-rest-framework.org/).

# Cómo montar una instancia

## Python

### Postgres

El servicio hace uso de una base de datos postgis. En la siguiente liga se
puede cosultar instrucciones para instalar los paquetes necesarios:

* [https://www.postgresql.org/docs/9.3/tutorial-install.html](postgres)
* [https://postgis.net/install/](postgis)

Una vez instalado postgres y postgis, se requiere crear una base de datos
y un usuario para el servicio. El nombre de la base de datos y usuario son
personalizable (se leen de las variables de ambiente `$POSTGRES_USER` y
`$POSTGRES_NAME`, para mas detalles ver `django_covid/settings.py`), pero
por omisión ambos son llamados 'covid_mexico'.

### Dependencias

Para instalar todos los requerimientos del servicio, correr

    pip install -f requirements.txt

### Migraciones y Actualizaciones

Antes de montar el servidor de desarrollo de django, hay que aplicar las
migraciones y actualizar los catalogos y casos:

    python manage.py migrate
    python manage.py actualizar_catalogos --descargar
    python manage.py actualizar_casos --descargar


#### Servidor de desarrollo

Para montar un servido de desarrollo local (en el puerto 8000) correr:

    python manage.py runserver 0.0.0.0:8000

o bien, para una versión más adecuada en un ambiente de producción:

    gunicorn django_covid.wsgi:application --bind 0.0.0.0:8000

## Docker Compose

Hemos incluido en el repositorio un par de archivos `docker-compose.yml`
para levantar nuevas instancias fácilmente en un sistema con 
[https://www.docker.com/](docker) instalado.

### Desarrollo

Para levantar una versión de desarrollo del API

    docker-compose up --build

Para inicializar la base de datos y el servicio de actualización

    docker-compose run covid_services bash iniciar.sh

El script de inicialización se encuentra en `docker/inciar.sh`.

### Producción

Antes de poder levantar una instacia de producción hay que crear
un archivo `.covid.prod.env` que declara el valor de las variables de ambiente
que contienen las credenciales de la base de datos. Se incluye `.covid.env` como
ejemplo.

Para levantar una versión de producción del API

    docker-compose -f docker-compose.prod.yml up --build

Para inicializar la base de datos y el servicio de actualización

    docker-compose run covid_services bash iniciar.sh

El script de inicialización se encuentra en `docker/inciar.prod.sh`.

### Actualización automatizada

Las imagenes de docker contienen las configuraciones de cron para correr
un script de actualización cada 2 horas. Las configuraciones del cron
está en `docker/cronjob`.

