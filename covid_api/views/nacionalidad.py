from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class NacionalidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = serializers.NacionalidadSerializer
    filterset_class = filters.NacionalidadFilter
