from covid_data import models
from covid_api import filters
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class TipoPacienteViewSet(CatalogoViewSet):
    queryset = models.TipoPaciente.objects.all()
    serializer_class = otros.TipoPacienteSerializer
    filterset_class = filters.TipoPacienteFilter
