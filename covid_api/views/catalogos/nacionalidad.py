from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import otros
from covid_api.views.catalogos.base import CatalogoVista


class CatalogoNacionalidadVista(CatalogoVista):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = otros.NacionalidadSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Nacionalidad - Valores posibles.

        Regresa la lista de valores posibles para *nacionalidad*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host>/api/catalogos/nacionalidad/

        """
        return super().list(*args, **kwargs)
