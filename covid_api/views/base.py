from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import renderers
from rest_framework_csv.renderers import CSVRenderer


class CatalogoViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    page_size = None
    pagination_class = None
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]
