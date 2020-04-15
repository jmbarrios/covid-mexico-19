from rest_framework import viewsets
from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer

from covid_data import models
from covid_api import filters


class EntidadSerializer(serializers.HyperlinkedModelSerializer):
    casos = serializers.SerializerMethodField()

    class Meta:
        model = models.Entidad
        fields = [
            'url',
            'clave',
            'descripcion']
        extra_kwargs = {
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }

    def get_casos(self, obj):
        print(obj)
        return 'hola'


class MunicipioSerializer(serializers.ModelSerializer):
    entidad = EntidadSerializer(read_only=True)

    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion']
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


@geojson_serializer('geometria')
class MunicipioGeoSerializer(serializers.ModelSerializer):
    entidad = EntidadSerializer(read_only=True)

    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion',
            'geometria']
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Municipio.objects.all()
    filterset_class = filters.MunicipioFilter
    lookup_field = 'clave'

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return MunicipioSerializer
        return MunicipioGeoSerializer
