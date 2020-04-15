from covid_data import models
from covid_api import filters
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class SectorViewSet(CatalogoViewSet):
    queryset = models.Sector.objects.all()
    serializer_class = otros.SectorSerializer
    filterset_class = filters.SectorFilter
