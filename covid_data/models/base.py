from django.db import models


class ModeloBase(models.Model):
    agregado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
