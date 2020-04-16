from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class ResultadoViewSet(CatalogoViewSet):
    queryset = models.Resultado.objects.all()
    serializer_class = otros.ResultadoSerializer
