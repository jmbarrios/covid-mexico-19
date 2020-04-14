from covid_data.models import Caso, TipoPaciente
from rest_framework import serializers


class CasoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caso
        fields = ['fecha_actualizacion', 'origen', 'sector', 'entidad_um',
                  'sexo', 'entidad_nacimiento', 'entidad_residencia',
                  'municipio_residencia', 'tipo_paciente', 'fecha_ingreso',
                  'fecha_sintomas', 'fecha_defuncion', 'intubado', 'neumonia',
                  'edad', 'nacionalidad', 'embarazo', 'habla_lengua_indigena',
                  'diabetes', 'epoc', 'asma', 'inmusupr', 'hipertension',
                  'otras_com', 'cardiovascular', 'obesidad', 'renal_cronica',
                  'tabaquismo', 'otro_caso', 'resultado', 'migrante',
                  'pais_nacionalidad', 'pais_origen', 'uci']


class TipoPacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPaciente
        fields = '__all__'
