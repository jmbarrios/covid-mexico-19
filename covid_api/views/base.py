from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import renderers
from rest_framework_csv.renderers import CSVRenderer


class PaginatedCSVRenderer(CSVRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        return super().render(
            data['results'],
            media_type=media_type,
            renderer_context=renderer_context)


renderer_classes = [
    renderers.JSONRenderer,
    renderers.BrowsableAPIRenderer,
    PaginatedCSVRenderer
]


class ListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]


class CatalogoViewSet(ListViewSet):
    page_size = None
    pagination_class = None
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]
