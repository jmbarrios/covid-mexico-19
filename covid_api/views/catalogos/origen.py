from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoOrigenVista(CatalogoVista):
    queryset = models.Origen.objects.all()
    serializer_class = otros.OrigenSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Origen - Valores posibles.

        Regresa la lista de valores posibles para *origen*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/origen/

        """
        return super().list(*args, **kwargs)
