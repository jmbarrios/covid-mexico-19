
from rest_framework import renderers
from rest_framework import mixins
from rest_framework import viewsets

from covid_api.renderers import CSVRenderer
from covid_api.renderers import PaginatedCSVRenderer


class CatalogoVista(mixins.ListModelMixin, viewsets.GenericViewSet):
    page_size = None
    pagination_class = None
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]


class CatalogoVistaPaginada(mixins.ListModelMixin, viewsets.GenericViewSet):
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        PaginatedCSVRenderer]
