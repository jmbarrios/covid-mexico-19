from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from covid_data import models
from covid_api import serializers
from covid_api import filters



class SexoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sexo.objects.all()
    serializer_class = serializers.SexoSerializer
    filterset_class = filters.SexoFilter


class OrigenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Origen.objects.all()
    serializer_class = serializers.OrigenSerializer
    filterset_class = filters.OrigenFilter


class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sector.objects.all()
    serializer_class = serializers.SectorSerializer
    filterset_class = filters.SectorFilter


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    serializer_class = serializers.EntidadSerializer
    filterset_class = filters.EntidadFilter


class NacionalidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Nacionalidad.objects.all()
    serializer_class = serializers.NacionalidadSerializer
    filterset_class = filters.NacionalidadFilter


class TipoPacienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TipoPaciente.objects.all()
    serializer_class = serializers.TipoPacienteSerializer
    filterset_class = filters.TipoPacienteFilter


class ResultadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Resultado.objects.all()
    serializer_class = serializers.ResultadoSerializer
    filterset_class = filters.ResultadoFilter


class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Pais.objects.all()
    serializer_class = serializers.PaisSerializer
    filterset_class = filters.PaisFilter


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


class SiNoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SiNo.objects.all()
    serializer_class = serializers.SiNoSerializer
    filterset_class = filters.SiNoFilter


class CasoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Caso.objects.all()
    serializer_class = serializers.CasoSerializer
    filterset_class = filters.CasoFilter


class EntidadGeoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    serializer_class = serializers.EntidadGeoSerializer
    filterset_class = filters.EntidadFilter


# class MunicipioGeoViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Municipio.objects.all()
#     serializer_class = serializers.MunicipioGeoSerializer
#     filterset_class = filters.MunicipioFilter
