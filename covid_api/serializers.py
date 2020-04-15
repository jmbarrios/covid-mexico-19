from covid_data import models
from rest_framework import serializers


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


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
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


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Municipio
        fields = ['clave', 'clave_municipio',
                  'abreviatura', 'entidad', 'descripcion']


class SiNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiNo
        fields = ['clave', 'descripcion']


class CasoSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer(read_only=True)
    sector = SectorSerializer(read_only=True)
    entidad_um = EntidadSerializer(read_only=True)
    sexo = SexoSerializer(read_only=True)
    entidad_nacimiento = EntidadSerializer(read_only=True)
    entidad_residencia = EntidadSerializer(read_only=True)
    municipio_residencia = MunicipioSerializer(read_only=True)
    tipo_paciente = SiNoSerializer(read_only=True)
    intubado = SiNoSerializer(read_only=True)
    neumonia = SiNoSerializer(read_only=True)
    nacionalidad = NacionalidadSerializer(read_only=True)
    embarazo = SiNoSerializer(read_only=True)
    habla_lengua_indigena = SiNoSerializer(read_only=True)
    diabetes = SiNoSerializer(read_only=True)
    epoc = SiNoSerializer(read_only=True)
    asma = SiNoSerializer(read_only=True)
    inmusupr = SiNoSerializer(read_only=True)
    hipertension = SiNoSerializer(read_only=True)
    otras_com = SiNoSerializer(read_only=True)
    cardiovascular = SiNoSerializer(read_only=True)
    obesidad = SiNoSerializer(read_only=True)
    renal_cronica = SiNoSerializer(read_only=True)
    tabaquismo = SiNoSerializer(read_only=True)
    otro_caso = SiNoSerializer(read_only=True)
    resultado = ResultadoSerializer(read_only=True)
    migrante = SiNoSerializer(read_only=True)
    pais_nacionalidad = PaisSerializer(read_only=True)
    pais_origen = PaisSerializer(read_only=True)
    uci = SiNoSerializer(read_only=True)

    class Meta:
        model = models.Caso
        fields = ['fecha_actualizacion', 'origen', 'sector', 'entidad_um',
                  'sexo', 'entidad_nacimiento', 'entidad_residencia',
                  'municipio_residencia', 'tipo_paciente', 'fecha_ingreso',
                  'fecha_sintomas', 'fecha_defuncion', 'intubado', 'neumonia',
                  'edad', 'nacionalidad', 'embarazo', 'habla_lengua_indigena',
                  'diabetes', 'epoc', 'asma', 'inmusupr', 'hipertension',
                  'otras_com', 'cardiovascular', 'obesidad', 'renal_cronica',
                  'tabaquismo', 'otro_caso', 'resultado', 'migrante',
                  'pais_nacionalidad', 'pais_origen', 'uci']
