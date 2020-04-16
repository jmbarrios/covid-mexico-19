from django.db.models import Count, Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from covid_data import models
from covid_api import filters
from covid_api.views.base import renderer_classes
from covid_api.serializers import entidad


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Entidad.objects.all()
    filterset_class = filters.EntidadFilter
    lookup_field = 'clave'
    renderer_classes = renderer_classes

    @method_decorator(cache_page(60*60*2))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return entidad.EntidadSerializer
        return entidad.EntidadGeoSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

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
