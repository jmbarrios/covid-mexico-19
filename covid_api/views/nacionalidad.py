from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class NacionalidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = otros.NacionalidadSerializer
    filterset_class = filters.NacionalidadFilter
