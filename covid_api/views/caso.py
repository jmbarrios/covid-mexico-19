from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.views.base import renderer_classes
from covid_api.serializers import caso


class CasoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Caso.objects.all()
    filterset_class = filters.CasoFilter
    renderer_classes = renderer_classes

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return caso.CasoSlugSerializer
        return caso.CasoSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Listado de casos registrados con descriptores.

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host>/api/caso?edad_lt=65&fecha_defuncion_lt=2020-04-05
        """
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        """Detalle de información por caso.

        Despliega la información desglosada de cada caso accediendo por
        clave. Cada detalle contiene la información que se enlista abajo.
        Ejemplo para el objeto con clave 10:

            <host>/api/caso/10/
        """
        return super().retrieve(*args, **kwargs)
