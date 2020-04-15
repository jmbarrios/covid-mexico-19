from django_filters import FilterSet
from covid_data import models


class CasoFilter(FilterSet):
    class Meta:
        model = models.Caso
        fields = {
            'fecha_actualizacion': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'origen__descripcion': ['exact', 'contains'],
            'sector__descripcion': ['exact', 'contains'],
            'entidad_um__descripcion': ['exact', 'contains'],
            'sexo__descripcion': ['exact'],
            'entidad_nacimiento__descripcion': ['exact', 'contains'],
            'entidad_residencia__descripcion': ['exact', 'contains'],
            'municipio_residencia__descripcion': ['exact', 'contains'],
            'municipio_residencia__clave_municipio': ['exact'],
            'tipo_paciente__descripcion': ['exact', 'contains'],
            'fecha_ingreso': ['gt', 'lt', 'gte', 'lte'],
            'fecha_sintomas': ['gt', 'lt', 'gte', 'lte'],
            'fecha_defuncion': ['gt', 'lt', 'gte', 'lte'],
            'intubado__descripcion': ['exact'],
            'neumonia__descripcion': ['exact'],
            'edad': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'nacionalidad__descripcion': ['exact', 'contains'],
            'embarazo__descripcion': ['exact'],
            'habla_lengua_indigena__descripcion': ['exact'],
            'diabetes__descripcion': ['exact'],
            'epoc__descripcion': ['exact'],
            'asma__descripcion': ['exact'],
            'inmusupr__descripcion': ['exact'],
            'hipertension__descripcion': ['exact'],
            'otras_com__descripcion': ['exact'],
            'cardiovascular__descripcion': ['exact'],
            'obesidad__descripcion': ['exact'],
            'renal_cronica__descripcion': ['exact'],
            'tabaquismo__descripcion': ['exact'],
            'otro_caso__descripcion': ['exact'],
            'resultado__descripcion': ['exact', 'contains'],
            'migrante__descripcion': ['exact'],
            'pais_nacionalidad__descripcion': ['exact', 'contains'],
            'pais_nacionalidad__codigo': ['exact', 'contains'],
            'pais_nacionalidad__region': ['exact', 'contains'],
            'pais_origen__descripcion': ['exact', 'contains'],
            'pais_origen__codigo': ['exact', 'contains'],
            'pais_origen__region': ['exact', 'contains'],
            'uci__descripcion': ['exact']
        }
