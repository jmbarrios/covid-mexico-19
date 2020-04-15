from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class SiNoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SiNo.objects.all()
    serializer_class = serializers.SiNoSerializer
    filterset_class = filters.SiNoFilter
