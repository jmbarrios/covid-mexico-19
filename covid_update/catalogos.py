import os
import glob
import pandas as pd
from django.conf import settings

from covid_update.constantes import COL_CATALOGO
from covid_update.constantes import COL_FORMATO
from covid_update.constantes import COL_DESCRIPCION
from covid_update.constantes import ENTIDADES
from covid_update.constantes import RESULTADO
from covid_update.constantes import MUNICIPIO


def procesar_catalogos():
    ruta_catalogos, ruta_descriptores = obtener_rutas()

    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR)

    nombre_descriptores = os.path.join(
        directorio,
        'descriptores.csv')
    if not os.path.exists(nombre_descriptores):
        descriptores = cargar_descriptores(ruta_descriptores)
        descriptores.to_csv(nombre_descriptores)
    else:
        descriptores = pd.read_csv(nombre_descriptores)

    directorio = os.path.join(directorio, settings.CATALOGOS_DIR)
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    catalogos = descriptores[COL_CATALOGO].dropna().unique()
    for catalogo in catalogos:
        nombre_catalogo = os.path.join(
            directorio,
            f'{catalogo}.csv')

        if not os.path.exists(nombre_catalogo):
            catalogo_df = cargar_catalogo(ruta_catalogos, catalogo)
            catalogo_df.to_csv(nombre_catalogo)


def obtener_rutas():
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.DESCARGAS_DIR,
        'diccionario_datos_covid19')

    archivos = glob.glob(os.path.join(directorio, '*'))
    catalogos = [ruta for ruta in archivos if 'Catalogos' in ruta][0]
    descriptores = [ruta for ruta in archivos if 'Descriptores' in ruta][0]
    return catalogos, descriptores


def obtener_pagina(nombre_catalogo):
    if nombre_catalogo == ENTIDADES:
        return f'Catálogo de {nombre_catalogo}'

    return f'Catálogo {nombre_catalogo}'


def obtener_primer_renglon(nombre_catalogo):
    if nombre_catalogo == RESULTADO:
        return 1
    return 0


def cargar_descriptores(ruta):
    descriptores = pd.read_excel(ruta, index_col=0)

    def obtener_catalogo(nombre):
        try:
            return nombre.split(':')[1].strip().replace(' ', '')
        except:
            return None

    descriptores[COL_CATALOGO] = descriptores[COL_FORMATO].apply(obtener_catalogo)
    return descriptores


def cargar_catalogo(ruta, nombre):
    pagina = obtener_pagina(nombre)
    renglon = obtener_primer_renglon(nombre)

    catalogo = pd.read_excel(
                ruta,
                sheet_name=pagina,
                index_col=0,
                skiprows=renglon)

    # La tabla de catalogos de Resultado no tiene nombrada la columna
    # de descripción
    if nombre == RESULTADO:
        catalogo = catalogo.rename(columns=lambda x: COL_DESCRIPCION)

    # La tabla de municipios tiene varios renglones duplicados.
    # Se los quitamos
    if nombre == MUNICIPIO:
        catalogo = catalogo[~catalogo.index.duplicated(keep='first')]

    # Elimitar los espacios blancos
    if COL_DESCRIPCION in catalogo.columns:
        catalogo[COL_DESCRIPCION].apply(lambda x: x.strip())

    return catalogo
