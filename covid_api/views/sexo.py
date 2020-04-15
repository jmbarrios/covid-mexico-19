from covid_data import models
from covid_api import filters
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class SexoViewSet(CatalogoViewSet):
    queryset = models.Sexo.objects.all()
    serializer_class = otros.SexoSerializer
    filterset_class = filters.SexoFilter
