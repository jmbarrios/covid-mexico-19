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
    casos_positivos = serializers.IntegerField(
        help_text='Número de casos confirmados.')
    casos_negativos = serializers.IntegerField(
        help_text='Número de casos negativos.')
    casos_sospechosos = serializers.IntegerField(
        help_text='Número de casos sospechosos.')
    defunciones_confirmadas = serializers.IntegerField(
        help_text='Número de defunciones de casos confirmados.')
    defunciones_sospechosas = serializers.IntegerField(
        help_text='Número de defunciones de casos sospechosos')
    intubados_confirmados = serializers.IntegerField(
        help_text='Número de casos confirmados que han sido intubados')
    intubados_sospechosos = serializers.IntegerField(
        help_text='Número de casos sospechosos que han sido intubados')
    hospitalizados_confirmados = serializers.IntegerField(
        help_text='Número de casos confirmados que han sido hospitalizados')
    hospitalizados_sospechosos = serializers.IntegerField(
        help_text='Número de casos sospechosos que han sido hospitalizados')
    ambulatorios_confirmados = serializers.IntegerField(
        help_text='Número de casos confirmados que son ambulatorios')
    ambulatorios_sospechosos = serializers.IntegerField(
        help_text='Número de casos sospechosos que son ambulatorios')
    criticos_confirmados = serializers.IntegerField(
        help_text='Número de casos confirmados que has sido ingresados a una unidad de cuidados intensivos')
    criticos_sospechosos = serializers.IntegerField(
        help_text='Número de casos sospechosos que has sido ingresados a una unidad de cuidados intensivos')

    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad',
            'descripcion',
            'casos_positivos',
            'casos_negativos',
            'casos_sospechosos',
            'defunciones_confirmadas',
            'defunciones_sospechosas',
            'intubados_confirmados',
            'intubados_sospechosos',
            'hospitalizados_confirmados',
            'hospitalizados_sospechosos',
            'ambulatorios_confirmados',
            'ambulatorios_sospechosos',
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
            'casos_positivos',
            'casos_negativos',
            'casos_sospechosos',
            'defunciones_confirmadas',
            'defunciones_sospechosas',
            'intubados_confirmados',
            'intubados_sospechosos',
            'hospitalizados_confirmados',
            'hospitalizados_sospechosos',
            'ambulatorios_confirmados',
            'ambulatorios_sospechosos',
            'criticos_confirmados',
            'criticos_sospechosos',
        ]
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


MunicipioGeoSerializer.__name__ = 'MunicipioGeoSerializer'
