import os

from django.db import models
from django.conf import settings


CASOS_DIR = os.path.join(
    settings.BASE_DIR,
    settings.DATOS_BASE_DIR,
    settings.CASOS_DIR)

LOGS_DIR = os.path.join(
    settings.BASE_DIR,
    settings.DATOS_BASE_DIR,
    settings.LOGS_DIR)


class Actualizacion(models.Model):
    ultima_actualizacion = models.DateField(auto_now_add=True)
    archivo = models.FilePathField(path=CASOS_DIR)
    log = models.FilePathField(path=LOGS_DIR, null=True)
