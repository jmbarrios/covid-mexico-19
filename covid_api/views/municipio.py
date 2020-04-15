from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data import models
from covid_api import serializers
from covid_api import filters


class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Municipio
    queryset = models.Municipio.objects.all()
    serializer_class = serializers.MunicipioSerializer
    filterset_class = filters.MunicipioFilter

    @action(detail=True, methods=['GET'], name='geometria')
    def geometria(self, request, pk=None):
        municipio = self.get_object()
        serializer = serializers.MunicipioGeoSerializer(municipio)
        return Response(serializer.data)
