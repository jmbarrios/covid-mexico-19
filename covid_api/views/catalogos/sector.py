from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import otros
from covid_api.views.catalogos.base import CatalogoVista


class CatalogoSectorVista(CatalogoVista):
    queryset = models.Sector.objects.all()
    serializer_class = otros.SectorSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Sector - Valores posibles.

        Regresa la lista de valores posibles para *sector*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host>/api/catalogos/sector/

        """
        return super().list(*args, **kwargs)
