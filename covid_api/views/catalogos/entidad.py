from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import entidad
from covid_api.views.catalogos.base import CatalogoVista


campos = ['clave', 'descripcion']


class CatalogoEntidadesVista(CatalogoVista):
    queryset = models.Entidad.objects.only(*campos).all()
    serializer_class = entidad.EntidadSimpleSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Entidad - Valores posibles.

        Regresa la lista de valores posibles para *Entidad*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host>/api/catalogos/entidades/

        """
        return super().list(*args, **kwargs)
