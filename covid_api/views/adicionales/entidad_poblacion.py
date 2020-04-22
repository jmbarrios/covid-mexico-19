from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data.models.municipio import COLUMNAS_GEOMETRIA
from covid_datos_adicionales.models import EntidadPoblacion
from covid_api.views.base import ListRetrieveViewSet
from covid_api.filters.adicional import EntidadPoblacionFilter
from covid_api.serializers.adicional.entidad_poblacion import EntidadPoblacionSerializer
from covid_api.serializers.adicional.entidad_poblacion import EntidadPoblacionListSerializer
from covid_api.serializers.adicional.entidad_poblacion import CAMPOS_EXTRA


defer = [
    f'entidad__{col}' for col in COLUMNAS_GEOMETRIA
]


class EntidadPoblacionViewSet(ListRetrieveViewSet):
    """
    Población por entidad.

    En este endpoint podrás acceder a la información de la población agregada
    a nivel entidad.

    La lista de entidades contiene sólo información de poblacion total,
    población masculina total y población femenina total. Pero si se desea un
    listado que incluya todos los datos poblacionales se puede usar el endpoint

        /api/poblacion/entidades/completo

    O bien, si se desean los datos poblacionales de una entidad en particular
    se puede consultar el endpoint

        /api/poblacion/entidades/<clave_entidad>

    Los datos fueron generados a partir de las proyecciones oficiales de
    población por municipio de la CONAPO e INEGI para el 2020.
    Se agregaron las poblaciones por entidad para cada grupo de edad, y se
    recalcularon los porcentajes. El código utilizado para su generación
    está en

        /covid_api/migrations/0002_entidades.py
    """
    queryset = (
        EntidadPoblacion.objects
        .prefetch_related('entidad')
        .defer(*defer)
        .all())
    filterset_class = EntidadPoblacionFilter
    serializer_class = EntidadPoblacionSerializer
    ordering = ['entidad__clave']
    ordering_fields = [
        'entidad__clave',
        'entidad__descripcion',
        'pt',
        'pmt',
        'pft'
    ]

    lookup_field = 'entidad__clave'
    lookup_url_kwarg = 'entidad'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        if self.action == 'list':
            queryset = queryset.defer(*CAMPOS_EXTRA)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EntidadPoblacionListSerializer
        return EntidadPoblacionSerializer

    def retrieve(self, *args, **kwargs):
        """
        Detalle de datos de población por entidad

        Los datos fueron generados a partir de las proyecciones oficiales de
        población por municipio de la CONAPO e INEGI para el 2020.
        Se agregaron las poblaciones por entidad para cada grupo de edad, y se
        recalcularon los porcentajes. El código utilizado para su generación
        está en

            /covid_api/migrations/0002_entidades.py
        """
        return super().retrieve(*args, **kwargs)

    def list(self, *args, **kwargs):
        """
        Listado de entidades con población total, masculina y femenina

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host:port>/api/poblacion/entidades?pt_gt=10000&ppft_gt=50

        Los datos fueron generados a partir de las proyecciones oficiales de
        población por municipio de la CONAPO e INEGI para el 2020.
        Se agregaron las poblaciones por entidad para cada grupo de edad, y se
        recalcularon los porcentajes. El código utilizado para su generación
        está en

            /covid_api/migrations/0002_entidades.py
        """
        return super().list(*args, **kwargs)

    @action(detail=False)
    def completo(self, request, **kwargs):
        """
        Listado de entidades con datos completos de población

        El conjunto de datos puede ser filtrado de acuerdo a los parámetros
        que se describen en el listado de abajo para producir subconjuntos de
        interés en la respuesta. Ejemplo:

            <host:port>/api/poblacion/entidades/completo?pt_gt=10000&ppft_gt=50

        Los datos fueron generados a partir de las proyecciones oficiales de
        población por municipio de la CONAPO e INEGI para el 2020.
        Se agregaron las poblaciones por entidad para cada grupo de edad, y se
        recalcularon los porcentajes. El código utilizado para su generación
        está en

            /covid_api/migrations/0002_entidades.py
        """
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
