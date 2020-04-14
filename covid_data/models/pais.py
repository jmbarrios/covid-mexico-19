from django.db import models
from covid_data.models.base import ModeloBase


class Pais(ModeloBase):
    nombre = models.CharField(max_length=80)
    codigo = models.CharField(max_length=3)
    region = models.CharField(max_length=31)
