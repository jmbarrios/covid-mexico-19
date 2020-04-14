from django.db import models
from covid_data.models.base import ModeloBase


class Origen(ModeloBase):
    """La vigilancia centinela se realiza a través del sistema de unidades
    de salud monitoras de enfermedades respiratorias (USMER). Las USMER
    incluyen unidades médicas del primer, segundo o tercer nivel de atención y
    también participan como USMER las unidades de tercer nivel que por sus
    características contribuyen a ampliar el panorama de información
    epidemiológica, entre ellas las que cuenten con especialidad de neumología,
    infectología o pediatría. (Categorías en Catalógo Anexo).
    """

    clave = models.IntegerField(unique=True)
    valor = models.CharField(max_length=63)
