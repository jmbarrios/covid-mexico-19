from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import otros
from covid_api.views.catalogos.base import CatalogoVista


class CatalogoPaisVista(CatalogoVista):
    queryset = models.Pais.objects.all()
    serializer_class = otros.PaisSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Pais - Valores posibles.

        Regresa la lista de paises del mundo asociados a la información por
        clave. No requiere parámetros. Ejemplo:

            <host>/api/catalogos/paises/

        """
        return super().list(*args, **kwargs)
