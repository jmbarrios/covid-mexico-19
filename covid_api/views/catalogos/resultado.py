from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoResultadoVista(CatalogoVista):
    queryset = models.Resultado.objects.all()
    serializer_class = otros.ResultadoSerializer

    def list(self, *args, **kwargs):
        """
        Resultado - Valores posibles.

        Regresa la lista de valores posibles para *resultado*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/resultado/

        """
        return super().list(*args, **kwargs)
