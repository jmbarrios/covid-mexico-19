from django.db import models
from django.contrib.gis.db.models import MultiPolygonField
from covid_data.models.base import ModeloBase


class Municipio(ModeloBase):
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=80)

    clave_municipio = models.IntegerField()
    entidad = models.ForeignKey(
        'Entidad',
        on_delete=models.CASCADE)
    geometria = MultiPolygonField()
