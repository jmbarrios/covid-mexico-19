from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import municipio


class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Municipio.objects.all()
    filterset_class = filters.MunicipioFilter
    lookup_field = 'clave'

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Listado de municipios de la República Mexicana.

        Regresa la lista de municipios con la clave de asociación usada en el
        modelo de 'caso' junto con descriptores y el número de casos
        registrados hasta el momento. Ejemplo\:

            <host>/api/municipio?casos_gt=100&descripcion_contiene=Oaxaca de Juárez

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        """Detalle de información por municipio.

        Despliega la información desglosada de cada municipio accediendo por
        clave. Cada detalle incluye la información que se enlista abajo. El
        campo de geometría se presenta en la proyección WGS 84 /
        Pseudo-Mercator (EPSG:3857). Ejemplo para el municipio con clave 230:

            <host>/api/municipio/230/

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().retrieve(*args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return municipio.MunicipioSerializer
        return municipio.MunicipioGeoSerializer
