from django.db import models
from covid_data.models.base import ModeloBase


class TipoPaciente(ModeloBase):
    """Identifica el tipo de atención que recibió el paciente en la unidad.
    Se denomina como ambulatorio si regresó a su casa o se denomina como
    hospitalizado si fue ingresado a hospitalización.
    """

    clave = models.IntegerField(unique=True)
    valor = models.CharField(max_length=63)
