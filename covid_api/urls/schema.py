from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

description = """
## API REST para la consulta de casos COVID-19 en México.

Estos servicios presetan la información liberada diariamente por la Dirección
General de Epidemiología de la Secretaría de Salud de la República Mexicana
referente a la actual epidemia de COVID-19. La fuente de datos es descargada y
formateada en tiempo real al momento de su liberación desde la fuente.

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
        <host>/api/caso?edad = 40
2. Cuando se usan los atributos 'clave' o 'descripcion' en comparación
exacta se indica con doble guión bajo el acceso al atributo. Ejemplo\:
        <host>/api/caso?sexo_descripcion=F
3. Cuando se usan los comparadores en combinación con los casos anteriores como
en los siguientes ejemplos\:
        <host>/api/caso?fecha_ingreso_gt=2020-04-12
        <host>/api/caso?municipio_residencia_descripcion_contiene=Mazatlán
        <host>/api/caso?edad_lt=60

En la documentación de cada modelo se especifican los parámetros para producir
filtros en cada modelo.

### Formato de respuesta

Para especificar el formato de respuesta deseado (*json* o *csv*), en cualquier
petición de listado se agrega el parámetro *format*. Por omisión, los
resultados se regresan en formato *json*. Ejemplo:

    <host>/api/casos?format=json

### Paginación

La paginación se especifica con los parámetros habituales *limit* y *offset*
para determinar el número máximo de registros retornados y la posición desde
la cual comienza la página en el resultado completo, respectivamente. Por
ejemplo, para solicitar 100 casos a partir de la posición 10 debería
de usarse\:

    <host>/api/casos?limit=100&offset=10

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
