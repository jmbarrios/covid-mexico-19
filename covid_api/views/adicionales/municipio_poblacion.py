from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data.models.municipio import COLUMNAS_GEOMETRIA
from covid_datos_adicionales.models import MunicipioPoblacion
from covid_api.views.base import ListRetrieveViewSet
from covid_api.filters.adicional import MunicipioPoblacionFilter
from covid_api.serializers.adicional.municipio_poblacion import MunicipioPoblacionSerializer
from covid_api.serializers.adicional.municipio_poblacion import MunicipioPoblacionListSerializer
from covid_api.serializers.adicional.municipio_poblacion import CAMPOS_EXTRA


defer = [
    f'municipio__{col}' for col in COLUMNAS_GEOMETRIA
] + [
    f'municipio__entidad__{col}' for col in COLUMNAS_GEOMETRIA
]


class MunicipioPoblacionViewSet(ListRetrieveViewSet):
    """
    Población por municipio.

    En este endpoint podrás acceder a la información de la población agregada
    a nivel municipio.

    La lista de municipios contiene sólo información de poblacion total,
    población masculina total y población femenina total. Pero si se desea un
    listado que incluya todos los datos poblacionales se puede usar el endpoint

        /api/poblacion/municipios/completo

    O bien, si se desean los datos poblacionales de un municipio en particular
    se puede consultar el endpoint

        /api/poblacion/municipios/<clave_municipio>

    Los datos fueron tomados de las proyecciones oficiales de población por
    municipio de la CONAPO e INEGI para el 2020.
    """
    queryset = (
        MunicipioPoblacion.objects
        .prefetch_related('municipio', 'municipio__entidad')
        .defer(*defer)
        .all())
    filterset_class = MunicipioPoblacionFilter
    serializer_class = MunicipioPoblacionSerializer
    lookup_field = 'municipio__clave'
    lookup_url_kwarg = 'municipio'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        if self.action == 'list':
            queryset = queryset.defer(*CAMPOS_EXTRA)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return MunicipioPoblacionListSerializer
        return MunicipioPoblacionSerializer

    def retrieve(self, *args, **kwargs):
        """
        Detalle de datos de población por municipio

        Los datos fueron tomados de las proyecciones oficiales de población por
        municipio de la CONAPO e INEGI para el 2020.
        """
        return super().retrieve(*args, **kwargs)

    def list(self, *args, **kwargs):
        """
        Listado de municipios con población total, masculina y femenina

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host:port>/api/poblacion/municipios?pt_gt=10000&ppft_gt=50

        Los datos fueron tomados de las proyecciones oficiales de población por
        municipio de la CONAPO e INEGI para el 2020.
        """
        return super().list(*args, **kwargs)

    @action(detail=False)
    def todo(self, request, **kwargs):
        """
        Listado de municipios con datos completos de población

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host:port>/api/poblacion/municipios/completo?pt_gt=10000&ppft_gt=50

        Los datos fueron tomados de las proyecciones oficiales de población por
        municipio de la CONAPO e INEGI para el 2020.
        """
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
