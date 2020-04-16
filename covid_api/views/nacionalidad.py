from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoViewSet


class NacionalidadViewSet(CatalogoViewSet):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = otros.NacionalidadSerializer
