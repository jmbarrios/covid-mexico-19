from django.db import models
from covid_data.models.base import ModeloBase


class Nacionalidad(ModeloBase):
    """Identifica si el paciente es mexicano o extranjero."""
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=63)

    def __repr__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion
