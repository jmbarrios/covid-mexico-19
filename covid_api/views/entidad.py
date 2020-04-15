from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from geojson_serializer.serializers import geojson_serializer

from covid_data import models
from covid_api import filters


class EntidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Entidad
        fields = ['url', 'clave', 'descripcion']


@geojson_serializer('geometria')
class EntidadGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entidad
        fields = ['clave', 'descripcion', 'geometria']


class EntidadViewSet(viewsets.ModelViewSet):
    queryset = models.Entidad.objects.all()
    serializer_class = EntidadSerializer
    filterset_class = filters.EntidadFilter

    @action(detail=True, methods=['GET'], name='geometria')
    def geometria(self, request, pk=None):
        entidad = self.get_object()
        serializer = EntidadGeoSerializer(entidad)
        return Response(serializer.data)
