from rest_framework_filters import FilterSet
from covid_data.models import Caso


class CasoFilter(FilterSet):
    class Meta:
        model = Caso
        fields = {
            'fecha_actualizacion': ['gt', 'lt', 'gte', 'lte'],
            'origen__valor': ['exact', 'contains'],
            'sector__valor': ['exact', 'contains'],
            'entidad_um__nombre': ['exact', 'contains'],
            'sexo': ['exact'],
            'entidad_nacimiento__nombre': ['exact', 'contains'],
            'entidad_residencia__nombre': ['exact', 'contains'],
            'municipio_residencia__nombre': ['exact', 'contains'],
            'municipio_residencia__clave_municipio': ['exact'],
            'municipio_residencia__abreviatura': ['exact', 'contains'],
            'tipo_paciente__valor': ['exact', 'contains'],
            'fecha_ingreso': ['gt', 'lt', 'gte', 'lte'],
            'fecha_sintomas': ['gt', 'lt', 'gte', 'lte'],
            'fecha_defuncion': ['gt', 'lt', 'gte', 'lte'],
            'intubado': ['exact'],
            'neumonia': ['exact'],
            'edad': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'nacionalidad': ['exact', 'contains'],
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
            'resultado__valor': ['exact', 'contains'],
            'migrante': ['exact'],
            'pais_nacionalidad__nombre': ['exact', 'contains'],
            'pais_nacionalidad__codigo': ['exact', 'contains'],
            'pais_nacionalidad__region': ['exact', 'contains'],
            'pais_origen__nombre': ['exact', 'contains'],
            'pais_origen__codigo': ['exact', 'contains'],
            'pais_origen__region': ['exact', 'contains'],
            'uci': ['exact']
        }
