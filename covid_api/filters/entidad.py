from django.db.models import Count, Q
import django_filters
from covid_data import models


class EntidadFilter(django_filters.FilterSet):
    casos__gt = django_filters.NumberFilter(
        help_text='Número de casos confirmados(mayor que)',
        method='casos_mayor_que')
    clave = django_filters.NumberFilter(
        help_text='Clave de entidad')
    descripcion = django_filters.CharFilter(
        field_name='descripcion',
        help_text='Nombre de entidad')
    descripcion__contiene = django_filters.CharFilter(
        field_name='descripcion',
        lookup_expr='icontains',
        help_text='Nombre de entidad (contiene)')

    class Meta:
        model = models.Entidad
        fields = [
            'clave',
            'descripcion',
            'descripcion__contiene',
            'casos__gt']

    def casos_mayor_que(self, queryset, name, value):
        filtro = Q(entidad_residencia__resultado__clave=1)
        return (
            queryset
            .annotate(casos_positivos=Count(
                'entidad_residencia',
                filter=filtro))
            .filter(casos_positivos__gt=value))
