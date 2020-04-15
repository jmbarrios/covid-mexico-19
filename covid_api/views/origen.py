from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class OrigenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Origen.objects.all()
    serializer_class = otros.OrigenSerializer
    filterset_class = filters.OrigenFilter
