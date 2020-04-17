from django.db.models import Count, Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.views.base import renderer_classes
from covid_api.serializers import entidad


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    serializer_class = entidad.EntidadSerializer
    lookup_field = 'clave'
    renderer_classes = renderer_classes
    ordering = ['-casos_positivos']
    ordering_fields = [
        'casos_positivos',
        'casos_negativos',
        'casos_sospechosos',
        'defunciones_confirmadas',
        'defunciones_sospechosas',
        'intubados_confirmados',
        'intubados_sospechosos',
        'hospitalizados_confirmados',
        'hospitalizados_sospechosos',
        'ambulatorios_confirmados',
        'ambulatorios_sospechosos',
        'criticos_confirmados',
        'criticos_sospechosos',
        'clave',
    ]

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        """
        Listado de entidades de la República Mexicana.

        Regresa la lista de estados con la clave de asociación usada en el
        modelo de 'caso' junto con descriptores y el número de casos
        registrados hasta el momento. Ejemplo\:

            <host:port>/api/entidad?casos_gt=100&descripcion_contiene=Veracruz

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        """Detalle de información por entidad.

        Despliega la información desglosada de cada entidad accediendo por
        clave. Cada detalle incluye la información que se enlista abajo. El
        campo de geometría se presenta en EPSG:4326. Ejemplo para la entidad
        con clave 15:

            <host:port>/api/entidad/15/

        Fuente\: https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=889463674658
        """
        return super().retrieve(*args, **kwargs)

    @action(detail=False, serializer_class=entidad.EntidadGeoSerializer)
    def geo(self, request, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {
                "type": "FeatureCollection",
                "features": serializer.data
            }
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, serializer_class=entidad.EntidadCentroideSerializer)
    def centroide(self, request, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {
                "type": "FeatureCollection",
                "features": serializer.data
            }
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, serializer_class=entidad.EntidadGeoSerializer)
    def shape(self, request, **kwargs):
        entidad = self.get_object()
        serializador = self.get_serializer(entidad)
        return Response(serializador.data)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        if self.action in ['list', 'retrieve']:
            queryset = queryset.defer('geometria', 'geometria_web')
        else:
            queryset = queryset.defer('geometria_web')

        cuenta_positivos = Count(
            'entidad_residencia',
            filter=Q(entidad_residencia__resultado__clave=1))
        cuenta_negativos = Count(
            'entidad_residencia',
            filter=Q(entidad_residencia__resultado__clave=2))
        cuenta_sospechosos = Count(
            'entidad_residencia',
            filter=Q(entidad_residencia__resultado__clave=3))

        cuenta_defunciones_confirmadas = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=1,
                entidad_residencia__fecha_defuncion__isnull=False))
        cuenta_defunciones_sospechosas = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=3,
                entidad_residencia__fecha_defuncion__isnull=False))

        cuenta_intubados_confirmados = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=1,
                entidad_residencia__intubado__clave=1))
        cuenta_intubados_sospechosos = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=3,
                entidad_residencia__intubado__clave=1))

        cuenta_hospitalizados_confirmados = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=1,
                entidad_residencia__tipo_paciente__clave=2))
        cuenta_hospitalizados_sospechosos = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=3,
                entidad_residencia__tipo_paciente__clave=2))

        cuenta_ambulatorios_confirmados = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=1,
                entidad_residencia__tipo_paciente__clave=1))
        cuenta_ambulatorios_sospechosos = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=3,
                entidad_residencia__tipo_paciente__clave=1))

        cuenta_critico_confirmados = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=1,
                entidad_residencia__uci__clave=1))
        cuenta_critico_sospechosos = Count(
            'entidad_residencia',
            filter=Q(
                entidad_residencia__resultado__clave=3,
                entidad_residencia__uci__clave=1))

        return queryset.annotate(
            casos_positivos=cuenta_positivos,
            casos_negativos=cuenta_negativos,
            casos_sospechosos=cuenta_sospechosos,
            defunciones_confirmadas=cuenta_defunciones_confirmadas,
            defunciones_sospechosas=cuenta_defunciones_sospechosas,
            intubados_confirmados=cuenta_intubados_confirmados,
            intubados_sospechosos=cuenta_intubados_sospechosos,
            hospitalizados_confirmados=cuenta_hospitalizados_confirmados,
            hospitalizados_sospechosos=cuenta_hospitalizados_sospechosos,
            ambulatorios_confirmados=cuenta_ambulatorios_confirmados,
            ambulatorios_sospechosos=cuenta_ambulatorios_sospechosos,
            criticos_confirmados=cuenta_critico_confirmados,
            criticos_sospechosos=cuenta_critico_sospechosos)
