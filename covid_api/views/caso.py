from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data import models
from covid_api import filters
from covid_api.views.base import ListViewSet
from covid_api.serializers import caso


campos = [
    'renglon',
    'fecha_actualizacion',
    'fecha_ingreso',
    'fecha_sintomas',
    'fecha_defuncion',
    'edad',
]


campos_relacionales = [
    'origen',
    'sector',
    'entidad_um',
    'sexo',
    'entidad_nacimiento',
    'entidad_residencia',
    'municipio_residencia',
    'tipo_paciente',
    'intubado',
    'neumonia',
    'nacionalidad',
    'embarazo',
    'habla_lengua_indigena',
    'diabetes',
    'epoc',
    'asma',
    'inmusupr',
    'hipertension',
    'otras_com',
    'cardiovascular',
    'obesidad',
    'renal_cronica',
    'tabaquismo',
    'otro_caso',
    'resultado',
    'migrante',
    'pais_nacionalidad',
    'pais_origen',
    'uci',
]

only = campos + [f'{campo}__descripcion' for campo in campos_relacionales]


class CasoViewSet(ListViewSet):
    queryset = models.Caso.objects.all().prefetch_related(*campos_relacionales)
    filterset_class = filters.CasoFilter
    serializer_class = caso.CasoSerializer
    ordering = ['fecha_ingreso']
    ordering_fields = [
        'fecha_ingreso',
        'fecha_sintomas',
        'fecha_defuncion',
        'fecha_actualizacion',
        'edad',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action not in ['coords', 'geo']:
            queryset = queryset.only(*only)
        else:
            queryset = queryset.only(*only, 'municipio_residencia__centroide')

        return queryset

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Listado de casos registrados.

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host:port>/api/caso?edad_lt=65&fecha_defuncion_lt=2020-04-05
        """
        return super().list(*args, **kwargs)

    @action(detail=False, serializer_class=caso.CasoCoordsSerializer)
    def coords(self, request, **kwargs):
        """
        Listado de casos con coordenadas del centroide del municipio.

        Regresa la lista de casos incluyendo en la respuesta las coordenadas
        del centroide del municipio asociado como campos de punto flotante
        nombrados como *latitiud* y *longitud*.
        Ejemplo\:

            <host:port>/api/caso/coords?edad_lt=65&fecha_defuncion_lt=2020-04-05
        """
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, serializer_class=caso.CasoGeoSerializer)
    def centroide(self, request, **kwargs):
        """
        Listado de casos con coordenadas del centroide del municipio en GeoJSON.

        Regresa una colección de objetos en formato GeoJSON con los centroides
        de los municipios junto con los atributos del caso como propiedades.
        Ejemplo\:

            <host:port>/api/caso/centroide?edad_lt=65&fecha_defuncion_lt=2020-04-05

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {
                "type": "FeatureCollection",
                "features": serializer.data
            }
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
