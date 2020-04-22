from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoNacionalidadVista(CatalogoVista):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = otros.NacionalidadSerializer

    def list(self, *args, **kwargs):
        """
        Nacionalidad - Valores posibles.

        Regresa la lista de valores posibles para *nacionalidad*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/nacionalidad/

        """
        return super().list(*args, **kwargs)
