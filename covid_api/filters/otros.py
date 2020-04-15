from django_filters import FilterSet
from covid_data import models


class SexoFilter(FilterSet):
    class Meta:
        model = models.Sexo
        fields = ['clave', 'descripcion']


class OrigenFilter(FilterSet):
    class Meta:
        model = models.Origen
        fields = ['clave', 'descripcion']


class SectorFilter(FilterSet):
    class Meta:
        model = models.Sector
        fields = ['clave', 'descripcion']


class NacionalidadFilter(FilterSet):
    class Meta:
        model = models.Nacionalidad
        fields = ['clave', 'descripcion']


class TipoPacienteFilter(FilterSet):
    class Meta:
        model = models.TipoPaciente
        fields = ['clave', 'descripcion']


class ResultadoFilter(FilterSet):
    class Meta:
        model = models.Resultado
        fields = ['clave', 'descripcion']


class PaisFilter(FilterSet):
    class Meta:
        model = models.Pais
        fields = ['clave', 'codigo', 'region', 'descripcion']


class SiNoFilter(FilterSet):
    class Meta:
        model = models.SiNo
        fields = ['clave', 'descripcion']
