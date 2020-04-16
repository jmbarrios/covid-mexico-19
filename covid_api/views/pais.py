from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class PaisViewSet(CatalogoViewSet):
    queryset = models.Pais.objects.all()
    serializer_class = otros.PaisSerializer
