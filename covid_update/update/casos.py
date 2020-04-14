import os
import logging
import pandas as pd

from django.conf import settings
from django.db import transaction

from covid_data.models import Resultado
from covid_data.models import TipoPaciente
from covid_data.models import Sector
from covid_data.models import Origen
from covid_data.models import Pais
from covid_data.models import Entidad
from covid_data.models import Municipio


logging.basicConfig(level=logging.INFO)


@transaction.atomic
def actualizar_casos():
    ultimo_archivo = obtener_ultima_tabla()
    for _, renglon in ultimo_archivo.iterrows():
        buscar_o_crear_renglon(renglon)



def obtener_ultima_tabla():
    pass


def buscar_o_crear_renglon(renglon):
    pass
