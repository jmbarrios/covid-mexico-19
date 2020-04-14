from rest_framework import viewsets
from covid_data.models import Caso
from covid_data.models import TipoPaciente
from covid_api.serializers import CasoSerializer
from covid_api.serializers import TipoPacienteSerializer
from covid_api.filters import CasoFilter


class CasosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Caso.objects.all()
    # model = Caso
    serializer_class = CasoSerializer
    filterset_class = CasoFilter


class TipoPacientesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoPaciente.objects.all()
    # model = TipoPaciente
    serializer_class = TipoPacienteSerializer
