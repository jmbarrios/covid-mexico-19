from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Pais.objects.all()
    serializer_class = otros.PaisSerializer
    filterset_class = filters.PaisFilter
