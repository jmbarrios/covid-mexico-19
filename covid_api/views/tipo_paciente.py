from rest_framework import viewsets

from covid_data import models
from covid_api import serializers
from covid_api import filters


class TipoPacienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TipoPaciente.objects.all()
    serializer_class = serializers.TipoPacienteSerializer
    filterset_class = filters.TipoPacienteFilter
