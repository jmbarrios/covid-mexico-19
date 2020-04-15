from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer

from covid_data import models
from covid_api.serializers import entidad


class MunicipioSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion'
        ]
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


class MunicipioSerializer(serializers.ModelSerializer):
    entidad = entidad.EntidadSimpleSerializer(read_only=True)
    casos_confirmados = serializers.IntegerField()
    casos_sospechosos = serializers.IntegerField()
    casos_descartados = serializers.IntegerField()
    defunciones_confirmadas = serializers.IntegerField()
    defunciones_sospechosas = serializers.IntegerField()
    intubados_confirmados = serializers.IntegerField()
    intubados_sospechosos = serializers.IntegerField()
    casos_hospitalizados = serializers.IntegerField()
    casos_hospitalizados_sospechosos = serializers.IntegerField()
    casos_ambulatorios = serializers.IntegerField()
    casos_ambulatorios_sospechosos = serializers.IntegerField()
    criticos_confirmados = serializers.IntegerField()
    criticos_sospechosos = serializers.IntegerField()

    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion',
            'casos_confirmados',
            'casos_sospechosos',
            'casos_descartados',
            'defunciones_confirmadas',
            'defunciones_sospechosas',
            'intubados_confirmados',
            'intubados_sospechosos',
            'casos_hospitalizados',
            'casos_hospitalizados_sospechosos',
            'casos_ambulatorios',
            'casos_ambulatorios_sospechosos',
            'criticos_confirmados',
            'criticos_sospechosos',
        ]
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


@geojson_serializer('geometria')
class MunicipioGeoSerializer(MunicipioSerializer):
    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion',
            'geometria',
            'casos_confirmados',
            'casos_sospechosos',
            'casos_descartados',
            'defunciones_confirmadas',
            'defunciones_sospechosas',
            'intubados_confirmados',
            'intubados_sospechosos',
            'casos_hospitalizados',
            'casos_hospitalizados_sospechosos',
            'casos_ambulatorios',
            'casos_ambulatorios_sospechosos',
            'criticos_confirmados',
            'criticos_sospechosos',
        ]
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


MunicipioGeoSerializer.__name__ = 'MunicipioGeoSerializer'
