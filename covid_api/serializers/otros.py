from rest_framework import serializers
from covid_data import models


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sexo
        fields = ['id', 'clave', 'descripcion']


class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Origen
        fields = ['id', 'clave', 'descripcion']


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sector
        fields = ['id', 'clave', 'descripcion']


class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nacionalidad
        fields = ['id', 'clave', 'descripcion']


class TipoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPaciente
        fields = ['id', 'clave', 'descripcion']


class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resultado
        fields = ['id', 'clave', 'descripcion']


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pais
        fields = ['id', 'clave', 'codigo', 'region', 'descripcion']


class SiNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiNo
        fields = ['id', 'clave', 'descripcion']
