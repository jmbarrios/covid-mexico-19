import json
from rest_framework import serializers

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
        model = models.Entidad
        fields = [
            'url',
            'clave',
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
            'url': {'view_name': 'entidad-detail', 'lookup_field': 'clave'}
        }


class EntidadGeoSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        read_only=True,
        default='Feature')
    geometry = serializers.SerializerMethodField()
    properties = EntidadSerializer(source='*')

    class Meta:
        model = models.Entidad
        fields = [
            'type',
            'geometry',
            'properties'
        ]

    def get_geometry(self, obj):
        return json.loads(obj.geometria.geojson)
