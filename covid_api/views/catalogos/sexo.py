from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoSexoVista(CatalogoVista):
    queryset = models.Sexo.objects.all()
    serializer_class = otros.SexoSerializer

    def list(self, *args, **kwargs):
        """
        Sexo - Valores posibles.

        Regresa la lista de valores posibles para *sexo*, según el formato de
        la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/sexo/

        """
        return super().list(*args, **kwargs)
