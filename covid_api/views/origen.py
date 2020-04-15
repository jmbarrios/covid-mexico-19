from covid_data import models
from covid_api import filters
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class OrigenViewSet(CatalogoViewSet):
    queryset = models.Origen.objects.all()
    serializer_class = otros.OrigenSerializer
    filterset_class = filters.OrigenFilter
