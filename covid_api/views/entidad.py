from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data import models
from covid_api import filters
from covid_api.views.base import ListRetrieveViewSet
from covid_api.serializers import entidad


class EntidadViewSet(ListRetrieveViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    serializer_class = entidad.EntidadSerializer
    lookup_field = 'clave'
    ordering = ['clave']
    ordering_fields = [
        'clave',
        'descripcion'
    ]

    def list(self, *args, **kwargs):
        """
        Listado de entidades de la República Mexicana.

        Regresa la lista de estados con la clave de asociación usada en el
        modelo de *caso* junto con descriptores. Ejemplo\:

            <host:port>/api/entidad?descripcion_contiene=Veracruz

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().list(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        """Detalle de información por entidad.

        Despliega la información desglosada de cada entidad accediendo por
        clave. Ejemplo para la entidad con clave 15:

            <host:port>/api/entidad/15

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().retrieve(*args, **kwargs)

    @action(detail=False, serializer_class=entidad.EntidadGeoSerializer)
    def geo(self, request, **kwargs):
        """
        Listado de entidades de la República Mexicana con geometría.

        Regresa la lista de entidades incluyendo la geometría en formato
        *GeoJSON*.
        Ejemplo\:

            <host:port>/api/entidad/geo?casos_gt=100&descripcion_contiene=Veracruz

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

    @action(detail=False, serializer_class=entidad.EntidadCentroideSerializer)
    def centroide(self, request, **kwargs):
        """
        Listado de entidades de la República Mexicana con centroide.

        Regresa la lista de entidades incluyendo el centroide en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/entidad/centroide?casos_gt=100&descripcion_contiene=Veracruz

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
        serializer_class=entidad.EntidadGeoSerializer)
    def geo_detalle(self, request, **kwargs):
        """
        Detalle de información por entidad con geometría.

        Regresa el detalle de la entidad en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/entidad/15/geo

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        entidad = self.get_object()
        serializador = self.get_serializer(entidad)
        return Response(serializador.data)

    @action(
        url_name='centroide',
        url_path='centroide',
        name='centroide',
        detail=True,
        serializer_class=entidad.EntidadCentroideSerializer)
    def centroide_detalle(self, request, **kwargs):
        """
        Detalle de información por entidad con centroide.

        Regresa el detalle de la entidad en formato *GeoJSON*.
        Ejemplo\:

            <host:port>/api/entidad/15/centroide

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        entidad = self.get_object()
        serializador = self.get_serializer(entidad)
        return Response(serializador.data)
