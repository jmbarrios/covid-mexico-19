from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.serializers import entidad


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    lookup_field = 'clave'

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return entidad.EntidadSerializer
        return entidad.EntidadGeoSerializer
