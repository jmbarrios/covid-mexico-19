from django.db import models
from django.contrib.gis.db.models import MultiPolygonField, PointField

from covid_data.models.base import ModeloBase


COLUMNAS_GEOMETRIA = [
    'geometria',
    'geometria_simplificada',
    'geometria_web',
    'geometria_web_simplificada',
    'centroide',
    'centroide_web',
]


class Entidad(ModeloBase):
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=80)

    geometria = MultiPolygonField(srid=4326)
    geometria_simplificada = MultiPolygonField(srid=4326)

    geometria_web = MultiPolygonField(srid=3857)
    geometria_web_simplificada = MultiPolygonField(srid=3857)

    centroide = PointField(srid=4326)
    centroide_web = PointField(srid=3857)

    def __repr__(self):
        return self.descripcion

    def __str__(self):
        return self.descripcion
