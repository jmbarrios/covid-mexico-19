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

- **contiene**\: regresa verdadero si el valor contiene el texto ingresado.

*Para cualquier tipo de campo, si no se usan los comparadores, se asume que la
búsqueda es exacta.*

### Especificación de parámetros y filtros

El nombre de un parámetro a usar dentro del url se compone entonces de la misma
forma en todos las situaciones\:

1. Cuando el campo se usa para comparar el valor exacto directamente,
únicamente se usa el nombre del campo con la igualdad. Ejemplo\:
        <host:port>/api/caso?edad = 40
2. Cuando se usan los atributos 'clave' o 'descripcion' en comparación
exacta se indica un guión bajo el acceso al atributo. Ejemplo\:
        <host:port>/api/caso?sexo_descripcion=F
3. Cuando se usan los comparadores en combinación con los casos anteriores como
en los siguientes ejemplos\:
        <host:port>/api/caso?fecha_ingreso_gt=2020-04-12
        <host:port>/api/caso?municipio_residencia_descripcion_contiene=Mazatlán
        <host:port>/api/caso?edad_lt=60

En la documentación de cada modelo se especifican los parámetros para producir
filtros en cada modelo.

### Formato de respuesta

Para especificar el formato de respuesta deseado (*json* o *csv*), en cualquier
petición de listado se agrega la extensión deseada al nombre del modelo.
Por omisión, los resultados se regresan en formato *json*. Ejemplo de petición,
en formato CSV:

    <host:port>/api/casos.csv?edad_gt=60

### Paginación

La paginación se especifica con los parámetros habituales *limit* y *offset*
para determinar el número máximo de registros retornados y la posición desde
la cual comienza la página en el resultado completo, respectivamente. Por
ejemplo, para solicitar 100 casos a partir de la posición 10 debería
de usarse\:

    <host:port>/api/casos?limit=100&offset=10

Estos parámetros se combinan con cualquier filtro.
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
