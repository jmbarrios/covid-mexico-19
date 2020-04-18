from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api.serializers import municipio
from covid_api.filters.municipio import MunicipioSimpleFilter
from covid_api.views.base import ListViewSet


campos = [
    'clave',
    'clave_municipio',
    'entidad',
    'descripcion']


class CatalogoMunicipiosVista(ListViewSet):
    queryset = models.Municipio.objects.only(*campos).all()
    serializer_class = municipio.MunicipioSimpleSerializer
    filterset_class = MunicipioSimpleFilter

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Municipio - Valores posibles.

        Regresa la lista de valores posibles para *municipio*, según el
        formato de la información liberada.

        """
        return super().list(*args, **kwargs)
