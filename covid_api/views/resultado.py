from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class ResultadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Resultado.objects.all()
    serializer_class = serializers.ResultadoSerializer
    filterset_class = filters.ResultadoFilter
