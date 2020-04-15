from covid_data import models
from covid_api import filters
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class SiNoViewSet(CatalogoViewSet):
    queryset = models.SiNo.objects.all()
    serializer_class = otros.SiNoSerializer
    filterset_class = filters.SiNoFilter
