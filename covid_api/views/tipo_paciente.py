from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import otros


class TipoPacienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TipoPaciente.objects.all()
    serializer_class = otros.TipoPacienteSerializer
    filterset_class = filters.TipoPacienteFilter
