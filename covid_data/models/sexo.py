from django.db import models
from covid_data.models.base import ModeloBase


class Sexo(ModeloBase):
    """Identifica al sexo del paciente."""
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=63)
