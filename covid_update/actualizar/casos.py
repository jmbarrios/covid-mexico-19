import os
import glob
import logging
import datetime
import pandas as pd
from tqdm import tqdm

from django.conf import settings
from django.db import transaction
from django.db import connection

from covid_data import models
from covid_update.models import Actualizacion
from covid_update.actualizar.fechas import PARSERS_FECHA


FORMATO = '%(levelname)s:: %(message)s %(columna)s %(valor)s'
ENCODING = 'latin-1'

FECHA_ACTUALIZACION = 'FECHA_ACTUALIZACION'
ORIGEN = 'ORIGEN'
SECTOR = 'SECTOR'
ENTIDAD_UM = 'ENTIDAD_UM'
SEXO = 'SEXO'
ENTIDAD_NAC = 'ENTIDAD_NAC'
ENTIDAD_RES = 'ENTIDAD_RES'
MUNICIPIO_RES = 'MUNICIPIO_RES'
TIPO_PACIENTE = 'TIPO_PACIENTE'
FECHA_INGRESO = 'FECHA_INGRESO'
FECHA_SINTOMAS = 'FECHA_SINTOMAS'
FECHA_DEF = 'FECHA_DEF'
INTUBADO = 'INTUBADO'
NEUMONIA = 'NEUMONIA'
EDAD = 'EDAD'
NACIONALIDAD = 'NACIONALIDAD'
EMBARAZO = 'EMBARAZO'
HABLA_LENGUA_INDIG = 'HABLA_LENGUA_INDIG'
DIABETES = 'DIABETES'
EPOC = 'EPOC'
ASMA = 'ASMA'
INMUSUPR = 'INMUSUPR'
HIPERTENSION = 'HIPERTENSION'
OTRA_COM = 'OTRA_COM'
CARDIOVASCULAR = 'CARDIOVASCULAR'
OBESIDAD = 'OBESIDAD'
RENAL_CRONICA = 'RENAL_CRONICA'
TABAQUISMO = 'TABAQUISMO'
OTRO_CASO = 'OTRO_CASO'
RESULTADO = 'RESULTADO'
MIGRANTE = 'MIGRANTE'
PAIS_NACIONALIDAD = 'PAIS_NACIONALIDAD'
PAIS_ORIGEN = 'PAIS_ORIGEN'
UCI = 'UCI'

COLUMNAS_FECHA = {
    FECHA_ACTUALIZACION: 'fecha_actualizacion',
    FECHA_INGRESO: 'fecha_ingreso',
    FECHA_SINTOMAS: 'fecha_sintomas',
    FECHA_DEF: 'fecha_defuncion',
}

COLUMNAS_SI_NO = {
    INTUBADO: 'intubado',
    NEUMONIA: 'neumonia',
    EMBARAZO: 'embarazo',
    HABLA_LENGUA_INDIG: 'habla_lengua_indigena',
    DIABETES: 'diabetes',
    EPOC: 'epoc',
    ASMA: 'asma',
    INMUSUPR: 'inmusupr',
    HIPERTENSION: 'hipertension',
    OTRA_COM: 'otras_com',
    CARDIOVASCULAR: 'cardiovascular',
    OBESIDAD: 'obesidad',
    RENAL_CRONICA: 'renal_cronica',
    TABAQUISMO: 'tabaquismo',
    OTRO_CASO: 'otro_caso',
    MIGRANTE: 'migrante',
    UCI: 'uci',
}


COLUMNAS_MODELOS = {
    NACIONALIDAD: models.Nacionalidad,
    ORIGEN: models.Origen,
    ENTIDAD_UM: models.Entidad,
    ENTIDAD_NAC: models.Entidad,
    ENTIDAD_RES: models.Entidad,
    TIPO_PACIENTE: models.TipoPaciente,
    RESULTADO: models.Resultado,
    SEXO: models.Sexo,
    SECTOR: models.Sector,
}


def actualizar_casos(log=None, forzar=False):
    if log is None:
        logging.basicConfig(level=logging.INFO, format=FORMATO)
    else:
        logging.basicConfig(
            filename=log,
            filemode='w',
            level=logging.INFO,
            format=FORMATO)

    archivo = obtener_ultimo_archivo()
    es_nuevo = es_nuevo_archivo(archivo)

    if not es_nuevo and not forzar:
        return 1

    with transaction.atomic():
        if not es_nuevo:
            with transaction.atomic():
                actualizacion_previa = Actualizacion.objects.get(archivo=archivo)
                actualizacion_previa.delete()

        with transaction.atomic():
            borrar_casos_anteriores()

        with transaction.atomic():
            tabla = cargar_tabla(archivo)
            catalogos = cargar_catalogos()
            municipios = cargar_municipios()

            renglones = len(tabla)
            nuevos_casos = []
            with transaction.atomic():
                for num_renglon, renglon in tqdm(tabla.iterrows(), total=renglones):
                    datos = obtener_datos(renglon, catalogos, municipios)
                    nuevos_casos.append(models.Caso(
                        renglon=num_renglon,
                        **datos))
                models.Caso.objects.bulk_create(nuevos_casos)

        with transaction.atomic():
            guardar_actualizacion(archivo, log)

    return 0


def obtener_ultimo_archivo():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CASOS_DIR)
    tablas = glob.glob(os.path.join(directorio, '*.csv'))
    return sorted(tablas, key=extraer_fecha, reverse=True)[0]


def es_nuevo_archivo(archivo):
    return not Actualizacion.objects.filter(archivo=archivo).exists()


def borrar_casos_anteriores():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM covid_data_caso")


def cargar_tabla(ruta):
    return pd.read_csv(ruta, encoding=ENCODING)


def extraer_fecha(nombre):
    errores = []
    for parser in PARSERS_FECHA:
        try:
            return parser(nombre)
        except Exception as error:
            errores.append(error)

    raise ValueError(f'Fecha irreconocible: {nombre}. Errores: {errores}')


def cargar_catalogos():
    return {
        'Nacionalidad': cargar_catalogo_de_modelo(models.Nacionalidad),
        'Origen': cargar_catalogo_de_modelo(models.Origen),
        'Resultado': cargar_catalogo_de_modelo(models.Resultado),
        'Sector': cargar_catalogo_de_modelo(models.Sector),
        'Sexo': cargar_catalogo_de_modelo(models.Sexo),
        'SiNo': cargar_catalogo_de_modelo(models.SiNo),
        'TipoPaciente': cargar_catalogo_de_modelo(models.TipoPaciente),
        'Entidad': cargar_catalogo_de_modelo(models.Entidad),
    }


def cargar_municipios():
    only = ['clave_municipio', 'entidad']

    entidades = {
        entidad.id: entidad
        for entidad in models.Entidad.objects.only('id').all()
    }

    municipios = {}
    for municipio in models.Municipio.objects.only(*only).all():
        clave = municipio.clave_municipio
        entidad = entidades[municipio.entidad_id]
        municipios[(clave, entidad.clave)] = municipio

    return municipios


def cargar_catalogo_de_modelo(modelo, defer=None):
    return {
        instancia.clave: instancia
        for instancia in modelo.objects.only('clave', 'id').all()
    }


def obtener_datos(renglon, catalogos, municipios):
    return {
        'edad': int(renglon[EDAD]),
        'nacionalidad': buscar_catalogo(renglon, NACIONALIDAD, catalogos),
        'origen': buscar_catalogo(renglon, ORIGEN, catalogos),
        'resultado': buscar_catalogo(renglon, RESULTADO, catalogos),
        'sector': buscar_catalogo(renglon, SECTOR, catalogos),
        'sexo': buscar_catalogo(renglon, SEXO, catalogos),
        'tipo_paciente': buscar_catalogo(renglon, TIPO_PACIENTE, catalogos),
        'entidad_um': buscar_catalogo(renglon, ENTIDAD_UM, catalogos),
        'entidad_nacimiento': buscar_catalogo(renglon, ENTIDAD_NAC, catalogos),
        'entidad_residencia': buscar_catalogo(renglon, ENTIDAD_RES, catalogos),
        'municipio_residencia': obtener_municipio(renglon, municipios),
        'pais_nacionalidad': obtener_pais_nacionalidad(renglon),
        'pais_origen': obtener_pais_origen(renglon),
        **obtener_columnas_si_no(renglon, catalogos),
        **extraer_columnas_fecha(renglon)
    }


def extraer_columnas_fecha(renglon):
    return {
        campo: extraer_fecha_columna(renglon, columna)
        for columna, campo in COLUMNAS_FECHA.items()
    }


def extraer_fecha_columna(renglon, columna):
    try:
        valor = renglon[columna]
        return cast_fecha(valor)
    except Exception as error:
        extra = {'columna': columna, 'valor': valor}
        logging.warning(str(error).strip(), extra=extra)
        return None


def cast_fecha(fecha):
    if fecha == '9999-99-99':
        return None

    return datetime.date.fromisoformat(fecha)


def obtener_columnas_si_no(renglon, catalogos):
    return {
        campo: obtener_bool_columna(renglon, columna, catalogos)
        for columna, campo in COLUMNAS_SI_NO.items()
    }


def obtener_bool_columna(renglon, columna, catalogos):
    catalogo = catalogos['SiNo']
    clave = renglon[columna]

    try:
        return catalogo[clave]
    except Exception as error:
        extra = {
            'columna': columna,
            'valor': clave}
        logging.warning(str(error), extra=extra)
        return None


def obtener_pais_nacionalidad(renglon):
    return buscar_pais(renglon[PAIS_NACIONALIDAD])


def obtener_pais_origen(renglon):
    return buscar_pais(renglon[PAIS_ORIGEN])


def buscar_catalogo(renglon, columna, catalogos):
    clave = renglon[columna]
    catalogo = catalogos[COLUMNAS_MODELOS[columna].__name__]

    try:
        return catalogo[clave]
    except Exception as error:
        if clave != models.Caso.NO_ESPECIFICADO:
            extra = {
                'columna': columna,
                'valor': clave}
            logging.warning(str(error), extra=extra)
        return None


def obtener_municipio(renglon, municipios):
    consulta = (renglon[MUNICIPIO_RES], renglon[ENTIDAD_RES])
    try:
        return municipios[consulta]
    except Exception as error:
        if consulta[0] != 999:
            extra = {
                'columna': MUNICIPIO_RES,
                'valor': consulta}
            logging.warning(str(error), extra=extra)
        return None


def buscar_pais(nombre):
    try:
        return models.Pais.objects.filter(descripcion__icontains=nombre).first()
    except:
        pass

    try:
        return models.Pais.objects.filter(clave__icontains=nombre).first()
    except:
        pass

    extra = {
        'modelo': models.Pais.__name__,
        'consulta': {'nombre': nombre}}
    logging.warning('No se encontró un país', extra=extra)
    return None


def guardar_actualizacion(archivo, log):
    actualizacion = Actualizacion(archivo=archivo, log=log)
    actualizacion.save()
