from django.db import models
from covid_data.models.base import ModeloBase


class Resultado(ModeloBase):
    """Identifica el resultado del análisis de la muestra reportado por
    el  laboratorio de la Red Nacional de Laboratorios de Vigilancia
    Epidemiológica (INDRE, LESP y LAVE). (Catálogo de resultados diagnósticos
    anexo).
    """
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=63)
