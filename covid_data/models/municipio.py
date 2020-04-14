from django.db import models
from django.contrib.gis.db.models import MultiPolygonField
from covid_data.models.base import ModeloBase


class Municipio(ModeloBase):
    clave = models.IntegerField(unique=True)
    clave_municipio = models.IntegerField()
    abreviatura = models.CharField(max_length=2)
    entidad = models.ForeignKey(
        'Entidad',
        on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    geometria = MultiPolygonField()
