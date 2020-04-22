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
    class Meta:
        model = models.Entidad
        fields = [
            'url',
            'clave',
            'descripcion',
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
        return json.loads(obj.geometria_simplificada.geojson)


class EntidadCentroideSerializer(serializers.ModelSerializer):
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
        return json.loads(obj.centroide.geojson)
