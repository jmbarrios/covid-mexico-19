from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class SiNoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SiNo.objects.all()
    serializer_class = otros.SiNoSerializer
    filterset_class = filters.SiNoFilter
