import os
import logging
import pandas as pd

from django.conf import settings
from django.db import transaction

from covid_data import models
from covid_update.constantes import COL_DESCRIPCION


RESULTADO = 'RESULTADO'
TIPO_PACIENTE = 'TIPO_PACIENTE'
ORIGEN = 'ORIGEN'
SECTOR = 'SECTOR'
SI_NO = 'SI_NO'
NACIONALIDAD = 'NACIONALIDAD'
SEXO = 'SEXO'
CATALOGOS = {
    RESULTADO: models.Resultado,
    TIPO_PACIENTE: models.TipoPaciente,
    ORIGEN: models.Origen,
    SECTOR: models.Sector,
    SI_NO: models.SiNo,
    NACIONALIDAD: models.Nacionalidad,
    SEXO: models.Sexo
}

logging.basicConfig(level=logging.INFO)


@transaction.atomic
def actualizar_catalogos():
    for catalogo in CATALOGOS:
        logging.info('Actualizando el catalogo: %s', catalogo)
        actualizar_catalogo(catalogo)


def actualizar_catalogo(catalogo):
    df = cargar_catalogo(catalogo)
    modelo = CATALOGOS[catalogo]

    for clave, renglon in df.iterrows():
        descripcion = renglon[COL_DESCRIPCION]
        _, creado = modelo.objects.get_or_create(
            clave=clave,
            descripcion=descripcion.strip())

        if creado:
            logging.info(
                '[%s] Entrada registrada: clave=%s, descripcion=%s',
                catalogo,
                clave,
                descripcion)


def cargar_catalogo(nombre):
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CATALOGOS_DIR)
    nombre_archivo = os.path.join(directorio, f'{nombre}.csv')
    return pd.read_csv(nombre_archivo, index_col=0)
