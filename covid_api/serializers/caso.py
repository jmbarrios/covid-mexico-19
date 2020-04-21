import json
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
            'renglon',
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


class CasoGeoSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        read_only=True,
        default='Feature')
    geometry = serializers.SerializerMethodField()
    properties = CasoSerializer(source='*')

    class Meta:
        model = models.Entidad
        fields = [
            'type',
            'geometry',
            'properties'
        ]

    def get_geometry(self, obj):
        return json.loads(obj.municipio_residencia.centroide.geojson)


class CasoCoordsSerializer(CasoSerializer):
    latitud = serializers.FloatField(
        source='municipio_residencia.centroide.y',
        allow_null=True,
        help_text='Latitud del centroide del municipio de residencia.')
    longitud = serializers.FloatField(
        source='municipio_residencia.centroide.x',
        allow_null=True,
        help_text='Longitud del centroide del municipio de residencia.')

    class Meta:
        model = models.Caso
        fields = [
            'renglon',
            'latitud',
            'longitud',
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


class CasoConteoSerializer(serializers.Serializer):
    conteo = serializers.IntegerField()

    fecha_actualizacion = serializers.DateField(
        read_only=True, allow_null=True)
    fecha_ingreso = serializers.DateField(
        read_only=True, allow_null=True)
    fecha_sintomas = serializers.DateField(
        read_only=True, allow_null=True)
    fecha_defuncion = serializers.DateField(
        read_only=True, allow_null=True)

    edad = serializers.IntegerField(
        read_only=True, allow_null=True)

    origen = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='origen__descripcion')
    sector = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='sector__descripcion')
    entidad_um = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='entidad_um__descripcion')
    sexo = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='sexo__descripcion')
    entidad_nacimiento = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='entidad_nacimiento__descripcion')
    entidad_residencia = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='entidad_residencia__descripcion')
    municipio_residencia = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='municipio_residencia__descripcion')
    tipo_paciente = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='tipo_paciente__descripcion')
    intubado = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='intubado__descripcion')
    neumonia = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='neumonia__descripcion')
    nacionalidad = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='nacionalidad__descripcion')
    embarazo = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='embarazo__descripcion')
    habla_lengua_indigena = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='habla_lengua_indigena__descripcion')
    diabetes = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='diabetes__descripcion')
    epoc = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='epoc__descripcion')
    asma = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='asma__descripcion')
    inmusupr = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='inmusupr__descripcion')
    hipertension = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='hipertension__descripcion')
    otras_com = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='otras_com__descripcion')
    cardiovascular = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='cardiovascular__descripcion')
    obesidad = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='obesidad__descripcion')
    renal_cronica = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='renal_cronica__descripcion')
    tabaquismo = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='tabaquismo__descripcion')
    otro_caso = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='otro_caso__descripcion')
    resultado = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='resultado__descripcion')
    migrante = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='migrante__descripcion')
    pais_nacionalidad = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='pais_nacionalidad__descripcion')
    pais_origen = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='pais_origen__descripcion')
    uci = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='uci__descripcion')

    def __init__(self, *args, **kwargs):
        columnas = kwargs.pop('columnas', None)
        super().__init__(*args, **kwargs)

        if columnas is not None:
            columnas.append('conteo')
            permitidas = set(columnas)
            existentes = set(self.fields)
            for campo in existentes - permitidas:
                self.fields.pop(campo)
