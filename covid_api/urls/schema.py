from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

description = """
## API REST para la consulta de casos COVID-19 en México.

Estos servicios presetan la información liberada diariamente por la Dirección
General de Epidemiología de la Secretaría de Salud de la República Mexicana
referente a la actual epidemia de COVID-19. Los datos originales son
descargados desde la dirección:

http://187.191.75.115/gobmx/salud/datos_abiertos

Posteriormente, la información es formateada e ingresada al API como una
inserción atómica en bloque, de manera que no se regresan resultados de
actualizaciones parciales.

Todos los valores de los campos corresponden a lo establecido en el diccionario
de datos liberado en:

http://187.191.75.115/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip

### Comparadores
A través de este API se puede consultar la información haciendo filtros sobre
los campos definidos mediante los siguientes comparadores:

#### Campos numéricos o de fecha

- **gt** (mayor que)\: comparador **>**
- **gte** (mayor o igual que)\: comparador **>=**
- **lt** (menor que)\: comparador **<**
- **lte** (menor o igual que)\: comparador **<=**

Para usar comparadores sobre fechas es necesario ingresar la fecha
usando el formato \:

    yyyy-mm-dd

#### Campos de texto

- **contiene**\: el registro es seleccionado si el valor contiene el texto ingresado.

*Para cualquier tipo de campo, si no se usan los comparadores, se asume que la
búsqueda es exacta.*

### Especificación de parámetros y filtros

El nombre de un parámetro dentro del url se compone de la misma
forma en todas las situaciones\:

1. Cuando el campo se usa para comparar el valor exacto directamente,
únicamente se emplea el nombre del campo con la igualdad. Ejemplo\:
        <host:port>/api/caso?edad=40
2. Cuando se usan los atributos *clave* o *descripcion* en comparación
exacta se indica con un guión bajo el acceso al atributo. Ejemplo\:
        <host:port>/api/caso?sexo_descripcion=MUJER
3. Usando los comparadores en combinación con los casos anteriores como
en los siguientes ejemplos\:
        <host:port>/api/caso?fecha_ingreso_gt=2020-04-12
        <host:port>/api/caso?municipio_residencia_descripcion_contiene=Mazatlán
        <host:port>/api/caso?edad_lt=60

En la documentación de cada punto de acceso se especifican los parámetros
para producir filtros específicos.

### Formato de respuesta

Para especificar el formato de respuesta deseado (*html*, *json* o *csv*), en
cualquier petición de listado se agrega la extensión deseada al final de la
ruta, antes de los parámetros de filtrado.
Por omisión, los resultados se regresan en formato *json*. Ejemplo de petición,
en formato CSV:

    <host:port>/api/casos.csv?edad_gt=60

### Paginación

La paginación se especifica con los parámetros habituales *limite* y *offset*
para determinar el número máximo de registros retornados y la posición desde
la cual comienza la página en el resultado completo, respectivamente. Por
ejemplo, para solicitar 100 casos a partir de la posición 10 debería
de usarse\:

    <host:port>/api/casos?limite=100&offset=10

Estos parámetros se combinan con cualquier filtro.

Los resultados paginados en formato JSON están estructurados de la siguiente
manera:

    {
        "total": número de entradas totales,
        "siguiente": url con la liga de la página siguiente,
        "previo": url con la liga de la página anterior,
        "results": [
            resultado de la consulta...
        ]
    }

**Los modelos *entidad*, *municipio* y *caso* son paginados por omisión**, por
lo que el número de resultados depende del tamaño de página, el cual se
controla con el parámetro *limite*. Para obtener la totalidad de los resultados
en una sola petición se asigna el valor de -1 a este parámetro

### Presentaciones espaciales

A través de distintos puntos de acceso, la información se sirve en
presentaciones que pueden ser útiles bajo contextos diferentes. Los puntos de
acceso **en la raíz** de cada modelo producen la **presentación por omisión**,
con campos simples, numéricos y de texto, y sin información geográfica
adicional. Cada una de las siguientes rutas secundarias produce una respuesta
alternativa, en caso de existir para el modelo dado:

- **geo**: producen respuestas en formato *GeoJSON* con la geometría de las
   coincidencias
- **centroide**: producen respuestas en formato *GeoJSON* con el centroide de la
   geometría asociada. Únicamente para el modelo 'caso', este campo corresponde
   al centroide del municipio asociado
- **coords**: produce respuestas con coordenadas geográficas en campos
   nombrados **latitud** y **longitud**. Por el momento, este endpoint está
   disponible únicamente para el modelo *caso*


Por el momento, todos los **campos espaciales se presentan en EPSG:4326**.
"""

schema_view = get_schema_view(
   openapi.Info(
      title="COVID-19 Mexico",
      default_version='v1',
      description=description,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(name="CONABIO"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
