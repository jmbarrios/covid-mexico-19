from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class SexoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sexo.objects.all()
    serializer_class = serializers.SexoSerializer
    filterset_class = filters.SexoFilter
