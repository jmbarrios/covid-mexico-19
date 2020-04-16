from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.views.base import renderer_classes
from covid_api.serializers import caso


class CasoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Caso.objects.all()
    filterset_class = filters.CasoFilter
    renderer_classes = renderer_classes

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return caso.CasoSlugSerializer
        return caso.CasoSerializer

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
