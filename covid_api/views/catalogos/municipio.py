from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import municipio
from covid_api.views.catalogos.base import CatalogoVista


campos = [
    'clave',
    'clave_municipio',
    'entidad',
    'descripcion']


class CatalogoMunicipiosVista(CatalogoVista):
    queryset = models.Municipio.objects.only(*campos).all()
    serializer_class = municipio.MunicipioSimpleSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Municipio - Valores posibles.

        Regresa la lista de valores posibles para *municipio*, según el
        formato de la información liberada.

        """
        return super().list(*args, **kwargs)
