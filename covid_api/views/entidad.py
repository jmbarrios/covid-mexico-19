from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import entidad


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    lookup_field = 'clave'

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Listado de entidades de la República Mexicana.

        Regresa la lista de estados con la clave de asociación usada en el
        modelo de 'caso' junto con descriptores y el número de casos
        registrados hasta el momento. Ejemplo\:

            <host>/api/entidad?casos_gt=100&descripcion_contiene=Veracruz

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        """Detalle de información por entidad.

        Despliega la información desglosada de cada entidad accediendo por
        clave. Cada detalle incluye la información que se enlista abajo. El
        campo de geometría se presenta en la proyección WGS 84 /
        Pseudo-Mercator (EPSG:3857). Ejemplo para la entidad con clave 15:

            <host>/api/entidad/15/

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().retrieve(*args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return entidad.EntidadSerializer
        return entidad.EntidadGeoSerializer
