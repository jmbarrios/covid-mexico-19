from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class ResultadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Resultado.objects.all()
    serializer_class = otros.ResultadoSerializer
    filterset_class = filters.ResultadoFilter
