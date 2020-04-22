import django_filters
from covid_data import models


class EntidadFilter(django_filters.FilterSet):
    clave = django_filters.NumberFilter(
        help_text='Clave de entidad')
    descripcion = django_filters.CharFilter(
        field_name='descripcion',
        help_text='Búsqueda exacta por descripción.')
    descripcion_contiene = django_filters.CharFilter(
        field_name='descripcion',
        lookup_expr='icontains',
        help_text='Búsqueda por descripción.')

    class Meta:
        model = models.Entidad
        fields = []
