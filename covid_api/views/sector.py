from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sector.objects.all()
    serializer_class = otros.SectorSerializer
    filterset_class = filters.SectorFilter
