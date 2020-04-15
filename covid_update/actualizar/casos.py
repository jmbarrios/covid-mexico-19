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


FECHA_REGEX_1 = re.compile(r'([0-9]{2}\.[0-9]{2}\.[0-9]{4})')
def extraer_fecha_1(nombre):
    fecha = FECHA_REGEX_1.search(nombre).group(0)
    dia, mes, año = fecha.split('.')
    return f'{año}-{mes}-{dia}'


FECHA_REGEX_2 = re.compile(r'(20[0-9]{2}[0-9]{4})')
def extraer_fecha_2(nombre):
    fecha = FECHA_REGEX_2.search(nombre).group(0)
    año = '20' + fecha[:2]
    mes = fecha[2:4]
    dia = fecha[4:]
    return f'{año}-{mes}-{dia}'


FORMATO = '%(levelname)s:: %(message)s %(modelo)s %(consulta)s'
ENCODING = 'latin-1'
PARSERS_FECHA = [
    extraer_fecha_1,
    extraer_fecha_2
]

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

COLUMNAS_RELACIONALES = {
    ORIGEN: 'origen',
    SECTOR: 'sector',
    ENTIDAD_UM: 'entidad_um',
    ENTIDAD_NAC: 'entidad_nacimiento',
    ENTIDAD_RES: 'entidad_residencia',
    MUNICIPIO_RES: 'municipio_residencia',
    TIPO_PACIENTE: 'tipo_paciente',
    RESULTADO: 'resultado',
    PAIS_NACIONALIDAD: 'pais_nacionalidad',
    PAIS_ORIGEN: 'pais_origen',
}

CAMPOS_ENTIDAD = {'entidad_um', 'entidad_nacimiento', 'entidad_residencia'}
CAMPOS_MUNICIPIO = {'municipio_residencia'}
CAMPOS_PAIS = {'pais_nacionalidad', 'pais_origen'}


@transaction.atomic
def actualizar_casos(log=None):
    if log is None:
        logging.basicConfig(level=logging.INFO, format=FORMATO)
    else:
        logging.basicConfig(
            filename=log,
            filemode='w',
            level=logging.INFO,
            format=FORMATO)

    ultima_tabla = obtener_ultima_tabla()

    renglones = len(ultima_tabla)
    nuevos_casos = []
    for _, renglon in tqdm(ultima_tabla.iterrows(), total=renglones):
        datos = obtener_datos(renglon)

        consulta = {
            **crear_consulta_relaciones(renglon),
            **crear_consulta(datos)}

        if not Caso.objects.filter(**consulta).exists():
            relaciones = obtener_relacionados(renglon)
            nuevos_casos.append(Caso(**datos, **relaciones))

    Caso.objects.bulk_create(nuevos_casos)


def extraer_fecha(nombre):
    for parser in PARSERS_FECHA:
        try:
            return parser(nombre)
        except:
            pass

    raise ValueError(f'Fecha irreconocible: {nombre}')


def obtener_ultima_tabla():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CASOS_DIR)
    tablas = glob.glob(os.path.join(directorio, '*.csv'))
    ruta = sorted(tablas, key=extraer_fecha, reverse=True)[0]
    return pd.read_csv(ruta, encoding=ENCODING)


def obtener_datos(renglon):
    return {
        'sexo': obtener_sexo(renglon),
        'edad': obtener_edad(renglon),
        'nacionalidad': obtener_nacionalidad(renglon),
        **extraer_columnas_booleanas(renglon),
        **extraer_columnas_fecha(renglon)
    }


def obtener_relacionados(renglon):
    return {
        'origen': obtener_origen(renglon),
        'sector': obtener_sector(renglon),
        'entidad_um': obtener_entidad_um(renglon),
        'entidad_nacimiento': obtener_entidad_nacimiento(renglon),
        'entidad_residencia': obtener_entidad_residencia(renglon),
        'municipio_residencia': obtener_municipio(renglon),
        'tipo_paciente': obtener_tipo_paciente(renglon),
        'resultado': obtener_resultado(renglon),
        'pais_nacionalidad': obtener_pais_nacionalidad(renglon),
        'pais_origen': obtener_pais_origen(renglon),
    }


def crear_consulta_relaciones(renglon):
    consulta = {}

    for columna, campo in COLUMNAS_RELACIONALES.items():
        if campo in CAMPOS_PAIS:
            continue

        valor = renglon[columna]
        if columna != MUNICIPIO_RES and valor == Caso.NO_ESPECIFICADO:
            consulta[f'{campo}__isnull'] = True
            continue

        if valor is None:
            consulta[f'{campo}__isnull'] = True
            continue

        if campo in CAMPOS_MUNICIPIO:
            consulta[f'{campo}__clave_municipio'] = valor
        else:
            consulta[f'{campo}__clave'] = valor

    return consulta


def crear_consulta(datos):
    consulta = {}

    for columna, valor in datos.items():
        if columna == 'fecha_actualizacion':
            continue

        if valor is None:
            consulta[f'{columna}__isnull'] = True
            continue

        consulta[columna] = valor

    return consulta


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
        valor = int(renglon[columna])
        return valor
    except Exception as error:
        extra = {'modelo': columna, 'consulta': valor}
        logging.warning(str(error).strip(), extra=extra)
        return None


def extraer_fecha_columna(renglon, columna):
    try:
        valor = renglon[columna]
        return cast_fecha(valor)
    except Exception as error:
        extra = {'modelo': columna, 'consulta': valor}
        logging.warning(str(error).strip(), extra=extra)
        return None


def cast_fecha(fecha):
    if fecha == '9999-99-99':
        return None

    return datetime.date.fromisoformat(fecha)


def obtener_origen(renglon):
    return buscar_modelo(renglon, {'clave': ORIGEN}, Origen)


def obtener_sector(renglon):
    return buscar_modelo(renglon, {'clave': SECTOR}, Sector)


def obtener_entidad_um(renglon):
    return buscar_modelo(renglon, {'clave': ENTIDAD_UM}, Entidad)


def obtener_sexo(renglon):
    return int(renglon[SEXO])


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
    return int(renglon[NACIONALIDAD])


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

    if 'clave' in consulta and modelo != Municipio:
        if consulta['clave'] == Caso.NO_ESPECIFICADO:
            return None

    try:
        return modelo.objects.get(**consulta)
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
