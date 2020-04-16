import os

from django.db import models
from django.conf import settings


def obtener_directorio_casos():
    return os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.CASOS_DIR)


def obtener_directorio_logs():
    return os.path.join(
        settings.BASE_DIR,
        settings.DATOS_BASE_DIR,
        settings.LOGS_DIR)


class Actualizacion(models.Model):
    ultima_actualizacion = models.DateField(auto_now_add=True)
    archivo = models.FilePathField(path=obtener_directorio_casos)
    log = models.FilePathField(path=obtener_directorio_logs, null=True)
