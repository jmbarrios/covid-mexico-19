import os
import glob
import re
import logging
import datetime
import pandas as pd
from tqdm import tqdm

from django.conf import settings
from django.db import transaction

from covid_data.models import Resultado
from covid_data.models import TipoPaciente
from covid_data.models import Sector
from covid_data.models import Origen
from covid_data.models import Pais
from covid_data.models import Caso
from covid_data.models import Entidad
from covid_data.models import Municipio


FORMATO = '%(levelname)s:: %(message)s %(modelo)s %(consulta)s'
ENCODING = 'latin-1'
FECHA_RE = re.compile(r'([0-9]{2}\.[0-9]{2}\.[0-9]{4})')

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
HABLA_LENGUA_INDI = 'HABLA_LENGUA_INDI'
DIABETES = 'DIABETES'
EPOC = 'EPOC'
ASMA = 'ASMA'
INMUSUPR = 'INMUSUPR'
HIPERTENSION = 'HIPERTENSION'
OTRA_CON = 'OTRA_CON'
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

COLUMNAS_BOOL = {
    INTUBADO: 'intubado',
    NEUMONIA: 'neumonia',
    EMBARAZO: 'embarazo',
    HABLA_LENGUA_INDI: 'habla_lengua_indigena',
    DIABETES: 'diabetes',
    EPOC: 'epoc',
    ASMA: 'asma',
    INMUSUPR: 'inmusupr',
    HIPERTENSION: 'hipertension',
    OTRA_CON: 'otras_com',
    CARDIOVASCULAR: 'cardiovascular',
    OBESIDAD: 'obesidad',
    RENAL_CRONICA: 'renal_cronica',
    TABAQUISMO: 'tabaquismo',
    OTRO_CASO: 'otro_caso',
    MIGRANTE: 'migrante',
    UCI: 'uci',
}

COLUMNAS_DET = [
    FECHA_ACTUALIZACION,
    ORIGEN,
    SECTOR,
    ENTIDAD_UM,
    SEXO,
    ENTIDAD_NAC,
    ENTIDAD_RES,
    MUNICIPIO_RES,
    TIPO_PACIENTE,
    FECHA_INGRESO,
    FECHA_SINTOMAS,
    FECHA_DEF,
    INTUBADO,
    NEUMONIA,
    EDAD,
    NACIONALIDAD,
    EMBARAZO,
    HABLA_LENGUA_INDI,
    DIABETES,
    EPOC,
    ASMA,
    INMUSUPR,
    HIPERTENSION,
    OTRA_CON,
    CARDIOVASCULAR,
    OBESIDAD,
    RENAL_CRONICA,
    TABAQUISMO,
    OTRO_CASO,
    RESULTADO,
    MIGRANTE,
    PAIS_NACIONALIDAD,
    PAIS_ORIGEN,
    UCI,
]


@transaction.atomic
def actualizar_casos(log=None):
    if log is None:
        logging.basicConfig(level=logging.INFO, format=FORMATO)
    else:
        logging.basicConfig(filename=log, level=logging.INFO, format=FORMATO)

    ultima_tabla = obtener_ultima_tabla()

    renglones = len(ultima_tabla)
    for _, renglon in tqdm(ultima_tabla.iterrows(), total=renglones):
        buscar_o_crear_renglon(renglon)

    raise Exception


def obtener_ultima_tabla():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CASOS_DIR)
    tablas = glob.glob(os.path.join(directorio, '*.csv'))
    ruta = sorted(tablas, key=extraer_fecha, reverse=True)[0]
    return pd.read_csv(ruta, encoding=ENCODING)


def extraer_fecha(nombre):
    fecha = FECHA_RE.search(nombre).group(0)
    dia, mes, año = fecha.split('.')
    return f'{año}-{mes}-{dia}'


def buscar_o_crear_renglon(renglon):
    datos = obtener_datos(renglon)
    caso, creado = Caso.objects.get_or_create(**datos)
    if creado:
        logging.info('Caso creado %s', caso, extra={'modelo': '', 'consulta': ''})
    return caso, creado


def obtener_datos(renglon):
    return {
        'origen': obtener_origen(renglon),
        'sector': obtener_sector(renglon),
        'entidad_um': obtener_entidad_um(renglon),
        'sexo': obtener_sexo(renglon),
        'entidad_nacimiento': obtener_entidad_nacimiento(renglon),
        'entidad_residencia': obtener_entidad_residencia(renglon),
        'municipio_residencia': obtener_municipio(renglon),
        'tipo_paciente': obtener_tipo_paciente(renglon),
        'edad': obtener_edad(renglon),
        'nacionalidad': obtener_nacionalidad(renglon),
        'resultado': obtener_resultado(renglon),
        'pais_nacionalidad': obtener_pais_nacionalidad(renglon),
        'pais_origen': obtener_pais_origen(renglon),
        **extraer_columnas_booleanas(renglon),
        **extraer_columnas_fecha(renglon)
    }


def extraer_columnas_booleanas(renglon):
    return {
        campo: extraer_bool_columna(renglon, columna)
        for columna, campo in COLUMNAS_BOOL.items()
    }


def extraer_columnas_fecha(renglon):
    return {
        campo: extraer_fecha_columna(renglon, columna)
        for columna, campo in COLUMNAS_FECHA.items()
    }


def extraer_bool_columna(renglon, columna):
    try:
        valor = renglon[columna]
        return cast_bool(valor)
    except Exception as error:
        extra = {'modelo': columna, 'consulta': valor}
        logging.warning(str(error).strip(), extra=extra)
        return None


def cast_bool(valor):
    if valor == 1:
        return True
    if valor == 2:
        return False

    raise ValueError('Valor inesperado')


def extraer_fecha_columna(renglon, columna):
    try:
        valor = renglon[columna]
        return cast_fecha(valor)
    except Exception as error:
        extra = {'modelo': columna, 'consulta': valor}
        logging.warning(str(error).strip(), extra=extra)
        return None


def cast_fecha(fecha):
    return datetime.date.fromisoformat(fecha)


def obtener_origen(renglon):
    return buscar_modelo(renglon, {'clave': ORIGEN}, Origen)


def obtener_sector(renglon):
    return buscar_modelo(renglon, {'clave': SECTOR}, Sector)


def obtener_entidad_um(renglon):
    return buscar_modelo(renglon, {'clave': ENTIDAD_UM}, Entidad)


def obtener_sexo(renglon):
    valor = renglon[SEXO]
    if valor == 1:
        return Caso.MUJER
    if valor == 2:
        return Caso.HOMBRE

    extra = {'modelo': SEXO, 'consulta': valor}
    logging.warning('Sexo', extra=extra)
    return None


def obtener_entidad_nacimiento(renglon):
    return buscar_modelo(renglon, {'clave': ENTIDAD_NAC}, Entidad)


def obtener_entidad_residencia(renglon):
    return buscar_modelo(renglon, {'clave': ENTIDAD_RES}, Entidad)


def obtener_municipio(renglon):
    consulta = {
        'clave_municipio': MUNICIPIO_RES,
        'entidad__clave': ENTIDAD_RES
    }
    return buscar_modelo(renglon, consulta, Municipio)


def obtener_tipo_paciente(renglon):
    return buscar_modelo(renglon, {'clave': TIPO_PACIENTE}, TipoPaciente)


def obtener_edad(renglon):
    return int(renglon[EDAD])


def obtener_nacionalidad(renglon):
    valor = renglon[ORIGEN]
    if valor == 1:
        return Caso.MEXICANA
    if valor == 2:
        return Caso.EXTRANJERA
    return None


def obtener_resultado(renglon):
    return buscar_modelo(renglon, {'clave': RESULTADO}, Resultado)


def obtener_pais_nacionalidad(renglon):
    return buscar_pais(renglon[PAIS_NACIONALIDAD])


def obtener_pais_origen(renglon):
    return buscar_pais(renglon[PAIS_ORIGEN])


def buscar_modelo(renglon, mapeo_consulta, modelo):
    consulta = {
        campo: renglon[columna]
        for campo, columna in mapeo_consulta.items()
    }

    try:
        modelo.objects.get(**consulta)
    except Exception as error:
        extra = {
            'modelo': modelo.__name__,
            'consulta': consulta}
        logging.warning(str(error), extra=extra)
        return None


def buscar_pais(nombre):
    try:
        return Pais.objects.filter(nombre__icontains=nombre).first()
    except:
        pass

    try:
        return Pais.objects.filter(codigo__icontains=nombre).first()
    except:
        pass

    extra = {
        'modelo': Pais.__nombre__,
        'consulta': {'nombre': nombre}}
    logging.warning('No se encontró un país', extra=extra)
    return None
