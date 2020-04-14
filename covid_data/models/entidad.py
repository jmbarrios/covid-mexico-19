from django.db import models
from django.contrib.gis.db.models import MultiPolygonField
from covid_data.models.base import ModeloBase


class Entidad(ModeloBase):
    clave = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=80)
    geometria = MultiPolygonField()
