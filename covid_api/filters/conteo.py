import django_filters
from covid_data import models
from covid_api.filters.caso import CasoFilter


COLUMNAS_CLAVE = {
    'entidad_um',
    'entidad_nacimiento',
    'entidad_residencia',
    'municipio_residencia',
}

COLUMNAS_DESCRIPCION = {
    *COLUMNAS_CLAVE,
    'origen',
    'sector',
    'sexo',
    'tipo_paciente',
    'intubado',
    'neumonia',
    'nacionalidad',
    'embarazo',
    'habla_lengua_indigena',
    'diabetes',
    'epoc',
    'asma',
    'inmusupr',
    'hipertension',
    'otras_com',
    'cardiovascular',
    'obesidad',
    'renal_cronica',
    'tabaquismo',
    'otro_caso',
    'resultado',
    'migrante',
    'pais_nacionalidad',
    'pais_origen',
    'uci',
}


COLUMNAS = {
    *COLUMNAS_DESCRIPCION,
    'fecha_actualizacion',
    'fecha_ingreso',
    'fecha_sintomas',
    'fecha_defuncion',
    'edad',
}


class CasoConteoFilter(CasoFilter):
    columna = django_filters.MultipleChoiceFilter(
        help_text='Columna sobre la cual se agrupan los casos.',
        choices=[(x, x) for x in list(COLUMNAS)],
        method='agregar_por_columnas')

    class Meta:
        model = models.Caso
        fields = []

    def agregar_por_columnas(self, queryset, name, value):
        cols = []
        for col in value:
            if col in COLUMNAS_CLAVE:
                cols += [f'{col}__descripcion', f'{col}__clave']
            elif col in COLUMNAS_DESCRIPCION:
                cols.append(f'{col}__descripcion')
            else:
                cols.append(col)
        print(cols)
        return queryset.values(*cols)
