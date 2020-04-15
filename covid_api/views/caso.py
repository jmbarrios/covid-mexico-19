from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework_csv.renderers import CSVRenderer

from covid_data import models
from covid_api.serializers import caso
from covid_api import filters


class CustomCSVRenderer(CSVRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        return super().render(
            data['results'],
            media_type=media_type,
            renderer_context=renderer_context)


class CasoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Caso.objects.all()
    filterset_class = filters.CasoFilter
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CustomCSVRenderer]

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
