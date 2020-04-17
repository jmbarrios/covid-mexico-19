from rest_framework import serializers

from covid_data import models


class CustomSlugField(serializers.SlugRelatedField):
    slug_field = 'descripcion'

    def __init__(self, *args, **kwargs):
        if 'slug_field' not in kwargs:
            kwargs['slug_field'] = self.slug_field

        super().__init__(*args, **kwargs)


class CasoSerializer(serializers.ModelSerializer):
    origen = CustomSlugField(read_only=True)
    sector = CustomSlugField(read_only=True)
    entidad_um = CustomSlugField(read_only=True)
    sexo = CustomSlugField(read_only=True)
    entidad_nacimiento = CustomSlugField(read_only=True)
    entidad_residencia = CustomSlugField(read_only=True)
    municipio_residencia = CustomSlugField(read_only=True)
    tipo_paciente = CustomSlugField(read_only=True)
    intubado = CustomSlugField(read_only=True)
    neumonia = CustomSlugField(read_only=True)
    nacionalidad = CustomSlugField(read_only=True)
    embarazo = CustomSlugField(read_only=True)
    habla_lengua_indigena = CustomSlugField(read_only=True)
    diabetes = CustomSlugField(read_only=True)
    epoc = CustomSlugField(read_only=True)
    asma = CustomSlugField(read_only=True)
    inmusupr = CustomSlugField(read_only=True)
    hipertension = CustomSlugField(read_only=True)
    otras_com = CustomSlugField(read_only=True)
    cardiovascular = CustomSlugField(read_only=True)
    obesidad = CustomSlugField(read_only=True)
    renal_cronica = CustomSlugField(read_only=True)
    tabaquismo = CustomSlugField(read_only=True)
    otro_caso = CustomSlugField(read_only=True)
    resultado = CustomSlugField(read_only=True)
    migrante = CustomSlugField(read_only=True)
    pais_nacionalidad = CustomSlugField(read_only=True)
    pais_origen = CustomSlugField(read_only=True)
    uci = CustomSlugField(read_only=True)

    class Meta:
        model = models.Caso
        fields = [
            'fecha_actualizacion',
            'fecha_ingreso',
            'fecha_sintomas',
            'fecha_defuncion',
            'edad',
            'origen',
            'sector',
            'entidad_um',
            'sexo',
            'entidad_nacimiento',
            'entidad_residencia',
            'municipio_residencia',
            'tipo_paciente',
            'intubado',
            'neumonia',
            'nacionalidad',
            'embarazo',
            'habla_lengua_indigena',
            'diabetes',
            'epoc',
            'asma',
            'inmusupr',
            'hipertension',
            'otras_com',
            'cardiovascular',
            'obesidad',
            'renal_cronica',
            'tabaquismo',
            'otro_caso',
            'resultado',
            'migrante',
            'pais_nacionalidad',
            'pais_origen',
            'uci']
