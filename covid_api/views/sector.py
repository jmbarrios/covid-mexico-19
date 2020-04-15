from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sector.objects.all()
    serializer_class = serializers.SectorSerializer
    filterset_class = filters.SectorFilter
