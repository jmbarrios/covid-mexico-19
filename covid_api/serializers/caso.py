from rest_framework import serializers

from covid_data import models
from covid_api.serializers import otros
from covid_api.serializers import entidad
from covid_api.serializers import municipio


class CustomSlugField(serializers.SlugRelatedField):
    slug_field = 'descripcion'

    def __init__(self, *args, **kwargs):
        if 'slug_field' not in kwargs:
            kwargs['slug_field'] = self.slug_field

        super().__init__(*args, **kwargs)


class CasoSlugSerializer(serializers.ModelSerializer):
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
            'id',
            'fecha_actualizacion',
            'origen',
            'sector',
            'entidad_um',
            'sexo',
            'entidad_nacimiento',
            'entidad_residencia',
            'municipio_residencia',
            'tipo_paciente',
            'fecha_ingreso',
            'fecha_sintomas',
            'fecha_defuncion',
            'intubado',
            'neumonia',
            'edad',
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


class CasoSerializer(serializers.ModelSerializer):
    origen = otros.OrigenSerializer(read_only=True)
    sector = otros.SectorSerializer(read_only=True)
    entidad_um = entidad.EntidadSimpleSerializer(read_only=True)
    sexo = otros.SexoSerializer(read_only=True)
    entidad_nacimiento = entidad.EntidadSimpleSerializer(read_only=True)
    entidad_residencia = entidad.EntidadSimpleSerializer(read_only=True)
    municipio_residencia = municipio.MunicipioSimpleSerializer(read_only=True)
    tipo_paciente = otros.SiNoSerializer(read_only=True)
    intubado = otros.SiNoSerializer(read_only=True)
    neumonia = otros.SiNoSerializer(read_only=True)
    nacionalidad = otros.NacionalidadSerializer(read_only=True)
    embarazo = otros.SiNoSerializer(read_only=True)
    habla_lengua_indigena = otros.SiNoSerializer(read_only=True)
    diabetes = otros.SiNoSerializer(read_only=True)
    epoc = otros.SiNoSerializer(read_only=True)
    asma = otros.SiNoSerializer(read_only=True)
    inmusupr = otros.SiNoSerializer(read_only=True)
    hipertension = otros.SiNoSerializer(read_only=True)
    otras_com = otros.SiNoSerializer(read_only=True)
    cardiovascular = otros.SiNoSerializer(read_only=True)
    obesidad = otros.SiNoSerializer(read_only=True)
    renal_cronica = otros.SiNoSerializer(read_only=True)
    tabaquismo = otros.SiNoSerializer(read_only=True)
    otro_caso = otros.SiNoSerializer(read_only=True)
    resultado = otros.ResultadoSerializer(read_only=True)
    migrante = otros.SiNoSerializer(read_only=True)
    pais_nacionalidad = otros.PaisSerializer(read_only=True)
    pais_origen = otros.PaisSerializer(read_only=True)
    uci = otros.SiNoSerializer(read_only=True)

    class Meta:
        model = models.Caso
        fields = [
            'id',
            'fecha_actualizacion',
            'origen',
            'sector',
            'entidad_um',
            'sexo',
            'entidad_nacimiento',
            'entidad_residencia',
            'municipio_residencia',
            'tipo_paciente',
            'fecha_ingreso',
            'fecha_sintomas',
            'fecha_defuncion',
            'intubado',
            'neumonia',
            'edad',
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
