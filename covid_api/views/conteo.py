from django.db.models import Count
from rest_framework.response import Response
from covid_data.models import Caso

from covid_api import filters
from covid_api.serializers.caso import CasoConteoSerializer
from covid_api.views.base import ListViewSet
from covid_api.views.caso import campos_relacionales
from covid_api.views.caso import only


class ConteoView(ListViewSet):
    queryset = (
        Caso.objects
        .all()
        .prefetch_related(*campos_relacionales)
        .only(*only, 'resultado__clave'))
    filterset_class = filters.CasoConteoFilter
    serializer_class = CasoConteoSerializer

    def list(self, request, *args, **kwargs):
        columnas = self.request.GET.getlist('columna')
        queryset = self.filter_queryset(self.get_queryset())

        if not columnas:
            queryset = queryset.aggregate(conteo=Count('renglon'))
            serializer = self.get_serializer(queryset, many=False, columnas=columnas)
            return Response(serializer.data)

        queryset = queryset.annotate(conteo=Count('renglon'))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True, columnas=columnas)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, columnas=columnas)
        return Response(serializer.data)
