from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import renderers

from covid_api.renderers import CSVRenderer


class ListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]


class ListRetrieveViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    renderer_classes = [
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer,
        CSVRenderer]
