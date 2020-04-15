from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class OrigenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Origen.objects.all()
    serializer_class = serializers.OrigenSerializer
    filterset_class = filters.OrigenFilter
