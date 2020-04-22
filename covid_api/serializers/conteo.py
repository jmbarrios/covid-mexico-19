from rest_framework import serializers


COLUMNAS_CLAVE = {
    'entidad_um',
    'entidad_nacimiento',
    'entidad_residencia',
    'municipio_residencia'}


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
    entidad_um_clave = serializers.IntegerField(
        read_only=True,
        allow_null=True,
        source='entidad_um__clave')
    sexo = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='sexo__descripcion')
    entidad_nacimiento = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='entidad_nacimiento__descripcion')
    entidad_nacimiento_clave = serializers.IntegerField(
        read_only=True,
        allow_null=True,
        source='entidad_nacimiento__clave')
    entidad_residencia = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='entidad_residencia__descripcion')
    entidad_residencia_clave = serializers.IntegerField(
        read_only=True,
        allow_null=True,
        source='entidad_residencia__clave')
    municipio_residencia = serializers.CharField(
        read_only=True,
        allow_null=True,
        source='municipio_residencia__descripcion')
    municipio_residencia_clave = serializers.IntegerField(
        read_only=True,
        allow_null=True,
        source='municipio_residencia__clave')
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
        columnas = kwargs.pop('columnas', [])
        columnas += [
            f'{col}_clave' for col in columnas
            if col in COLUMNAS_CLAVE]

        super().__init__(*args, **kwargs)

        if columnas is not None:
            columnas.append('conteo')
            permitidas = set(columnas)
            existentes = set(self.fields)
            for campo in existentes - permitidas:
                self.fields.pop(campo)
