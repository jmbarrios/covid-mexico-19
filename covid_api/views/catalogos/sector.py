from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoSectorVista(CatalogoVista):
    queryset = models.Sector.objects.all()
    serializer_class = otros.SectorSerializer

    def list(self, *args, **kwargs):
        """
        Sector - Valores posibles.

        Regresa la lista de valores posibles para *sector*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/sector/

        """
        return super().list(*args, **kwargs)
