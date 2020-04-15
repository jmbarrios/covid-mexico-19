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


class EntidadFilter(FilterSet):
    class Meta:
        model = models.Entidad
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


class MunicipioFilter(FilterSet):
    class Meta:
        model = models.Municipio
        fields = ['clave', 'clave_municipio', 'entidad', 'descripcion']


class SiNoFilter(FilterSet):
    class Meta:
        model = models.SiNo
        fields = ['clave', 'descripcion']


class CasoFilter(FilterSet):
    class Meta:
        model = models.Caso
        fields = {
            'fecha_actualizacion': ['gt', 'lt', 'gte', 'lte'],
            'origen__descripcion': ['exact', 'contains'],
            'sector__descripcion': ['exact', 'contains'],
            'entidad_um__descripcion': ['exact', 'contains'],
            'sexo': ['exact'],
            'entidad_nacimiento__descripcion': ['exact', 'contains'],
            'entidad_residencia__descripcion': ['exact', 'contains'],
            'municipio_residencia__descripcion': ['exact', 'contains'],
            'municipio_residencia__clave_municipio': ['exact'],
            'tipo_paciente__descripcion': ['exact', 'contains'],
            'fecha_ingreso': ['gt', 'lt', 'gte', 'lte'],
            'fecha_sintomas': ['gt', 'lt', 'gte', 'lte'],
            'fecha_defuncion': ['gt', 'lt', 'gte', 'lte'],
            'intubado': ['exact'],
            'neumonia': ['exact'],
            'edad': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'nacionalidad': ['exact'],
            'nacionalidad__descripcion': ['exact', 'contains'],
            'embarazo': ['exact'],
            'habla_lengua_indigena': ['exact'],
            'diabetes': ['exact'],
            'epoc': ['exact'],
            'asma': ['exact'],
            'inmusupr': ['exact'],
            'hipertension': ['exact'],
            'otras_com': ['exact'],
            'cardiovascular': ['exact'],
            'obesidad': ['exact'],
            'renal_cronica': ['exact'],
            'tabaquismo': ['exact'],
            'otro_caso': ['exact'],
            'resultado__descripcion': ['exact', 'contains'],
            'migrante': ['exact'],
            'pais_nacionalidad__descripcion': ['exact', 'contains'],
            'pais_nacionalidad__codigo': ['exact', 'contains'],
            'pais_nacionalidad__region': ['exact', 'contains'],
            'pais_origen__descripcion': ['exact', 'contains'],
            'pais_origen__codigo': ['exact', 'contains'],
            'pais_origen__region': ['exact', 'contains'],
            'uci': ['exact']
        }
