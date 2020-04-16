from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from covid_data import models
from covid_api import filters
from covid_api.views.base import renderer_classes
from covid_api.views.base import ListViewSet
from covid_api.serializers import caso


class CasoViewSet(ListViewSet):
    queryset = models.Caso.objects.all()
    filterset_class = filters.CasoFilter
    serializer_class = caso.CasoSerializer
    renderer_classes = renderer_classes
    ordering = ['fecha_ingreso']
    ordering_fields = [
        'fecha_ingreso',
        'fecha_sintomas',
        'fecha_defuncion',
        'fecha_actualizacion',
        'edad',
    ]

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
