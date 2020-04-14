import os
import logging
import pandas as pd

from django.conf import settings
from django.db import transaction

from covid_data.models import Resultado
from covid_data.models import TipoPaciente
from covid_data.models import Sector
from covid_data.models import Origen

from covid_update.constantes import COL_DESCRIPCION


RESULTADO = 'RESULTADO'
TIPO_PACIENTE = 'TIPO_PACIENTE'
ORIGEN = 'ORIGEN'
SECTOR = 'SECTOR'
CATALOGOS = [
    RESULTADO,
    TIPO_PACIENTE,
    ORIGEN,
    SECTOR,
]
MODELOS = {
    RESULTADO: Resultado,
    TIPO_PACIENTE: TipoPaciente,
    ORIGEN: Origen,
    SECTOR: Sector
}

logging.basicConfig(level=logging.INFO)


@transaction.atomic
def actualizar_catalogos():
    for catalogo in CATALOGOS:
        logging.info('Actualizando el catalogo: %s', catalogo)
        actualizar_catalogo(catalogo)


def actualizar_catalogo(catalogo):
    df = cargar_catalogo(catalogo)
    modelo = MODELOS[catalogo]

    for clave, renglon in df.iterrows():
        valor = renglon[COL_DESCRIPCION]
        _, creado = modelo.objects.get_or_create(clave=clave, valor=valor)

        if creado:
            logging.info(
                '[%s] Entrada registrada: clave=%s, valor=%s',
                catalogo,
                clave,
                valor)


def cargar_catalogo(nombre):
    directorio = os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CATALOGOS_DIR)
    nombre_archivo = os.path.join(directorio, f'{nombre}.csv')
    return pd.read_csv(nombre_archivo, index_col=0)
