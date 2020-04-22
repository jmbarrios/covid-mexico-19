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
    queryset = (
        EntidadPoblacion.objects
        .prefetch_related('entidad')
        .defer(*defer)
        .all())
    filterset_class = EntidadPoblacionFilter
    serializer_class = EntidadPoblacionSerializer
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

    @action(detail=False)
    def todo(self, request, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
