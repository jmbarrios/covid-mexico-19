from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data import models
from covid_api import filters
from covid_api.views.base import ListRetrieveViewSet
from covid_api.serializers import municipio


class MunicipioViewSet(ListRetrieveViewSet):
    queryset = models.Municipio.objects.all()
    filterset_class = filters.MunicipioFilter
    serializer_class = municipio.MunicipioSerializer
    lookup_field = 'clave'
    ordering = ['clave']
    ordering_fields = [
        'clave',
        'clave_municipio',
        'descripcion',
        'entidad__clave',
        'entidad__descripcion'
    ]

    @method_decorator(cache_page(60*60*2, cache="filesystem"))
    def list(self, *args, **kwargs):
        """
        Listado de municipios de la República Mexicana.

        Regresa la lista de municipios con la clave de asociación usada en el
        modelo de *caso* junto con descriptores y el número de casos
        registrados hasta el momento. Ejemplo\:

            <host:port>/api/municipio?casos_gt=100&descripcion_contiene=Oaxaca de Juárez

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().list(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        """Detalle de información por municipio.

        Despliega la información desglosada de cada municipio accediendo por
        clave. Ejemplo para el municipio con clave 230:

            <host:port>/api/municipio/230

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().retrieve(*args, **kwargs)

    @method_decorator(cache_page(60*60*2, cache="filesystem"))
    @action(detail=False, serializer_class=municipio.MunicipioGeoSerializer)
    def geo(self, request, **kwargs):
        """
        Listado de municipios de la República Mexicana con geometría.

        Regresa la lista de municipios incluyendo la geometría en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/municipio/geo?casos_gt=100&descripcion_contiene=Oaxaca de Juárez

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

    @method_decorator(cache_page(60*60*2, cache="filesystem"))
    @action(detail=False, serializer_class=municipio.MunicipioCentroideSerializer)
    def centroide(self, request, **kwargs):
        """
        Listado de municipios de la República Mexicana con centroide.

        Regresa la lista de municipios incluyendo el centroide en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/municipio/centroide?casos_gt=100&descripcion_contiene=Oaxaca de Juárez

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

    @action(
        url_name='geo',
        url_path='geo',
        name='geo',
        detail=True,
        serializer_class=municipio.MunicipioGeoSerializer)
    def geo_detalle(self, request, **kwargs):
        """
        Detalle de información por municipio con geometría.

        Regresa el detalle del municipio en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/municipio/230/geo

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        municipio = self.get_object()
        serializador = self.get_serializer(municipio)
        return Response(serializador.data)

    @action(
        url_name='centroide',
        url_path='centroide',
        name='centroide',
        detail=True,
        serializer_class=municipio.MunicipioCentroideSerializer)
    def centroide_detalle(self, request, **kwargs):
        """
        Detalle de información por municipio con centroide.

        Regresa el detalle del municipio en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/municipio/230/geo

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        municipio = self.get_object()
        serializador = self.get_serializer(municipio)
        return Response(serializador.data)
