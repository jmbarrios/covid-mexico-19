import json
from rest_framework import serializers
from covid_data import models


class MunicipioSerializer(serializers.ModelSerializer):
    entidad_clave = serializers.SlugRelatedField(
        read_only=True,
        source='entidad',
        slug_field='clave')
    entidad_descripcion = serializers.SlugRelatedField(
        read_only=True,
        source='entidad',
        slug_field='descripcion')
    entidad_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='entidad',
        view_name='entidad-detail',
        lookup_field='clave')

    class Meta:
        model = models.Municipio
        fields = [
            'url',
            'clave',
            'clave_municipio',
            'entidad_clave',
            'entidad_descripcion',
            'entidad_url',
            'descripcion'
        ]
        extra_kwargs = {
            'url': {'view_name': 'municipio-detail', 'lookup_field': 'clave'}
        }


class MunicipioGeoSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        read_only=True,
        default='Feature')
    geometry = serializers.SerializerMethodField()
    properties = MunicipioSerializer(source='*')

    class Meta:
        model = models.Entidad
        fields = [
            'type',
            'geometry',
            'properties'
        ]

    def get_geometry(self, obj):
        return json.loads(obj.geometria_simplificada.geojson)


class MunicipioCentroideSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        read_only=True,
        default='Feature')
    geometry = serializers.SerializerMethodField()
    properties = MunicipioSerializer(source='*')

    class Meta:
        model = models.Entidad
        fields = [
            'type',
            'geometry',
            'properties'
        ]

    def get_geometry(self, obj):
        return json.loads(obj.centroide.geojson)
