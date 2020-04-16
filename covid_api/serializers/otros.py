from rest_framework import serializers
from covid_data import models


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sexo
        fields = ['clave', 'descripcion']


class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Origen
        fields = ['clave', 'descripcion']


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sector
        fields = ['clave', 'descripcion']


class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nacionalidad
        fields = ['clave', 'descripcion']


class TipoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPaciente
        fields = ['clave', 'descripcion']


class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resultado
        fields = ['clave', 'descripcion']


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pais
        fields = ['clave', 'codigo', 'region', 'descripcion']


class SiNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiNo
        fields = ['clave', 'descripcion']
