from covid_data import models
from rest_framework import serializers


class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Origen
        fields = ['clave', 'valor']


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sector
        fields = ['clave', 'valor']


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
        fields = ['clave', 'nombre']


class CasoSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer(read_only=True)
    sector = SectorSerializer(read_only=True)
    entidad_um = EntidadSerializer(read_only=True)
    # sector = serializers.SlugRelatedField(read_only=True, slug_field='valor')
    # origen = serializers.SlugRelatedField(read_only=True, slug_field='valor')

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


class TipoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPaciente
        fields = '__all__'
