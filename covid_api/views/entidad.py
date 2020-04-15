from rest_framework import viewsets
from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer

from covid_data import models
from covid_api import filters


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
        fields = ['url', 'clave', 'descripcion']
        extra_kwargs = {
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


@geojson_serializer('geometria')
class EntidadGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
        fields = ['url', 'clave', 'descripcion', 'geometria']
        extra_kwargs = {
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    lookup_field = 'clave'

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return EntidadSerializer
        return EntidadGeoSerializer
