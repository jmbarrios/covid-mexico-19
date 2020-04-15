from django_filters import FilterSet
from covid_data import models


class MunicipioFilter(FilterSet):
    class Meta:
        model = models.Municipio
        fields = ['clave', 'clave_municipio', 'entidad', 'descripcion']
