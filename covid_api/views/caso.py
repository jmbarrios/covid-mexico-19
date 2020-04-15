from rest_framework import viewsets
from covid_data import models
from covid_api import serializers
from covid_api import filters


class CasoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Caso.objects.all()
    serializer_class = serializers.CasoSerializer
    filterset_class = filters.CasoFilter
