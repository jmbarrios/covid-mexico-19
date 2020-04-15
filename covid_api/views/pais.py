from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters



class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Pais.objects.all()
    serializer_class = serializers.PaisSerializer
    filterset_class = filters.PaisFilter
