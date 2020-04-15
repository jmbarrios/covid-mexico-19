from rest_framework import serializers
from geojson_serializer.serializers import geojson_serializer

from covid_data import models


class EntidadSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
        fields = [
            'url',
            'clave',
            'descripcion']
        extra_kwargs = {
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


class EntidadSerializer(serializers.ModelSerializer):
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
        model = models.Entidad
        fields = [
            'url',
            'clave',
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
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


@geojson_serializer('geometria')
class EntidadGeoSerializer(EntidadSerializer):
    class Meta:
        model = models.Entidad
        fields = [
            'url',
            'clave',
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
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


EntidadGeoSerializer.__name__ = 'EntidadGeoSerializer'
