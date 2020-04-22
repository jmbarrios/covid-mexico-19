import django_filters
from covid_datos_adicionales.models import MunicipioPoblacion


class MunicipioPoblacionFilter(django_filters.FilterSet):
    clave = django_filters.NumberFilter(
        field_name='municipio__clave',
        help_text='Búsqueda exacta por clave.')
    clave_municipio = django_filters.NumberFilter(
        field_name='municipio__clave_municipio',
        help_text='Búsqueda exacta por clave de municipio (dentro de la entidad.')

    descripcion = django_filters.CharFilter(
        field_name='municipio__descripcion',
        help_text='Búsqueda exacta por descripción).')
    descripcion_contiene = django_filters.CharFilter(
        field_name='municipio__descripcion',
        help_text='Búsqueda exacta por descripción.',
        lookup_expr='icontains')

    entidad_clave = django_filters.NumberFilter(
        field_name='municipio__entidad__clave',
        help_text=(
            'Entidad a la que pertenece el Municipio. Búsqueda por clave.'))
    entidad_descripcion = django_filters.CharFilter(
        field_name='municipio__entidad__descripcion',
        help_text=(
            'Entidad a la que pertenece el Municipio. '
            'Búsqueda exacta por descripción.'))
    entidad_descripcion_contiene = django_filters.CharFilter(
        field_name='municipio__entidad__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Entidad a la que pertenece el Municipio. '
            'Búsqueda por descripción.'))

    pm = django_filters.NumberFilter(
        help_text=(
            "Población masculina total"))
    pm_lt = django_filters.NumberFilter(
        field_name="pm",
        lookup_expr="lt",
        help_text=(
            "Población masculina total. Menor que."))
    pm_gt = django_filters.NumberFilter(
        field_name="pm",
        lookup_expr="gt",
        help_text=(
            "Población masculina total. Mayor que."))
    pm_lte = django_filters.NumberFilter(
        field_name="pm",
        lookup_expr="lte",
        help_text=(
            "Población masculina total. Menor o igual que."))
    pm_gte = django_filters.NumberFilter(
        field_name="pm",
        lookup_expr="gte",
        help_text=(
            "Población masculina total. Mayor o igual que."))
    ppm = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina total"))
    ppm_lt = django_filters.NumberFilter(
        field_name="ppm",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina total. Menor que."))
    ppm_gt = django_filters.NumberFilter(
        field_name="ppm",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina total. Mayor que."))
    ppm_lte = django_filters.NumberFilter(
        field_name="ppm",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina total. Menor o igual que."))
    ppm_gte = django_filters.NumberFilter(
        field_name="ppm",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina total. Mayor o igual que."))
    pf = django_filters.NumberFilter(
        help_text=(
            "Población femenina total"))
    pf_lt = django_filters.NumberFilter(
        field_name="pf",
        lookup_expr="lt",
        help_text=(
            "Población femenina total. Menor que."))
    pf_gt = django_filters.NumberFilter(
        field_name="pf",
        lookup_expr="gt",
        help_text=(
            "Población femenina total. Mayor que."))
    pf_lte = django_filters.NumberFilter(
        field_name="pf",
        lookup_expr="lte",
        help_text=(
            "Población femenina total. Menor o igual que."))
    pf_gte = django_filters.NumberFilter(
        field_name="pf",
        lookup_expr="gte",
        help_text=(
            "Población femenina total. Mayor o igual que."))
    ppf = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina total"))
    ppf_lt = django_filters.NumberFilter(
        field_name="ppf",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina total. Menor que."))
    ppf_gt = django_filters.NumberFilter(
        field_name="ppf",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina total. Mayor que."))
    ppf_lte = django_filters.NumberFilter(
        field_name="ppf",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina total. Menor o igual que."))
    ppf_gte = django_filters.NumberFilter(
        field_name="ppf",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina total. Mayor o igual que."))
    pt = django_filters.NumberFilter(
        help_text=(
            "Población total del municipio"))
    pt_lt = django_filters.NumberFilter(
        field_name="pt",
        lookup_expr="lt",
        help_text=(
            "Población total del municipio. Menor que."))
    pt_gt = django_filters.NumberFilter(
        field_name="pt",
        lookup_expr="gt",
        help_text=(
            "Población total del municipio. Mayor que."))
    pt_lte = django_filters.NumberFilter(
        field_name="pt",
        lookup_expr="lte",
        help_text=(
            "Población total del municipio. Menor o igual que."))
    pt_gte = django_filters.NumberFilter(
        field_name="pt",
        lookup_expr="gte",
        help_text=(
            "Población total del municipio. Mayor o igual que."))
    ppt = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de referencia, total"))
    ppt_lt = django_filters.NumberFilter(
        field_name="ppt",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de referencia, total. Menor que."))
    ppt_gt = django_filters.NumberFilter(
        field_name="ppt",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de referencia, total. Mayor que."))
    ppt_lte = django_filters.NumberFilter(
        field_name="ppt",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de referencia, total. Menor o igual que."))
    ppt_gte = django_filters.NumberFilter(
        field_name="ppt",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de referencia, total. Mayor o igual que."))
    pm0019 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 0 a 19 años"))
    pm0019_lt = django_filters.NumberFilter(
        field_name="pm0019",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 0 a 19 años. Menor que."))
    pm0019_gt = django_filters.NumberFilter(
        field_name="pm0019",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 0 a 19 años. Mayor que."))
    pm0019_lte = django_filters.NumberFilter(
        field_name="pm0019",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 0 a 19 años. Menor o igual que."))
    pm0019_gte = django_filters.NumberFilter(
        field_name="pm0019",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 0 a 19 años. Mayor o igual que."))
    ppm0019 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total"))
    ppm0019_lt = django_filters.NumberFilter(
        field_name="ppm0019",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total. Menor que."))
    ppm0019_gt = django_filters.NumberFilter(
        field_name="ppm0019",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total. Mayor que."))
    ppm0019_lte = django_filters.NumberFilter(
        field_name="ppm0019",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total. Menor o igual que."))
    ppm0019_gte = django_filters.NumberFilter(
        field_name="ppm0019",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total. Mayor o igual que."))
    pf0019 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 0 a 19 años"))
    pf0019_lt = django_filters.NumberFilter(
        field_name="pf0019",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 0 a 19 años. Menor que."))
    pf0019_gt = django_filters.NumberFilter(
        field_name="pf0019",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 0 a 19 años. Mayor que."))
    pf0019_lte = django_filters.NumberFilter(
        field_name="pf0019",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 0 a 19 años. Menor o igual que."))
    pf0019_gte = django_filters.NumberFilter(
        field_name="pf0019",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 0 a 19 años. Mayor o igual que."))
    ppf0019 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total"))
    ppf0019_lt = django_filters.NumberFilter(
        field_name="ppf0019",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total. Menor que."))
    ppf0019_gt = django_filters.NumberFilter(
        field_name="ppf0019",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total. Mayor que."))
    ppf0019_lte = django_filters.NumberFilter(
        field_name="ppf0019",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total. Menor o igual que."))
    ppf0019_gte = django_filters.NumberFilter(
        field_name="ppf0019",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total. Mayor o igual que."))
    pt0019 = django_filters.NumberFilter(
        help_text=(
            "Población total de 0 a 19 años"))
    pt0019_lt = django_filters.NumberFilter(
        field_name="pt0019",
        lookup_expr="lt",
        help_text=(
            "Población total de 0 a 19 años. Menor que."))
    pt0019_gt = django_filters.NumberFilter(
        field_name="pt0019",
        lookup_expr="gt",
        help_text=(
            "Población total de 0 a 19 años. Mayor que."))
    pt0019_lte = django_filters.NumberFilter(
        field_name="pt0019",
        lookup_expr="lte",
        help_text=(
            "Población total de 0 a 19 años. Menor o igual que."))
    pt0019_gte = django_filters.NumberFilter(
        field_name="pt0019",
        lookup_expr="gte",
        help_text=(
            "Población total de 0 a 19 años. Mayor o igual que."))
    ppt0019 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total"))
    ppt0019_lt = django_filters.NumberFilter(
        field_name="ppt0019",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total. Menor que."))
    ppt0019_gt = django_filters.NumberFilter(
        field_name="ppt0019",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total. Mayor que."))
    ppt0019_lte = django_filters.NumberFilter(
        field_name="ppt0019",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total. Menor o igual que."))
    ppt0019_gte = django_filters.NumberFilter(
        field_name="ppt0019",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total. Mayor o igual que."))
    pm2024 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 20 a 24 años"))
    pm2024_lt = django_filters.NumberFilter(
        field_name="pm2024",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 20 a 24 años. Menor que."))
    pm2024_gt = django_filters.NumberFilter(
        field_name="pm2024",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 20 a 24 años. Mayor que."))
    pm2024_lte = django_filters.NumberFilter(
        field_name="pm2024",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 20 a 24 años. Menor o igual que."))
    pm2024_gte = django_filters.NumberFilter(
        field_name="pm2024",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 20 a 24 años. Mayor o igual que."))
    ppm2024 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total"))
    ppm2024_lt = django_filters.NumberFilter(
        field_name="ppm2024",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total. Menor que."))
    ppm2024_gt = django_filters.NumberFilter(
        field_name="ppm2024",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total. Mayor que."))
    ppm2024_lte = django_filters.NumberFilter(
        field_name="ppm2024",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total. Menor o igual que."))
    ppm2024_gte = django_filters.NumberFilter(
        field_name="ppm2024",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total. Mayor o igual que."))
    pf2024 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 20 a 24 años"))
    pf2024_lt = django_filters.NumberFilter(
        field_name="pf2024",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 20 a 24 años. Menor que."))
    pf2024_gt = django_filters.NumberFilter(
        field_name="pf2024",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 20 a 24 años. Mayor que."))
    pf2024_lte = django_filters.NumberFilter(
        field_name="pf2024",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 20 a 24 años. Menor o igual que."))
    pf2024_gte = django_filters.NumberFilter(
        field_name="pf2024",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 20 a 24 años. Mayor o igual que."))
    ppf2024 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total"))
    ppf2024_lt = django_filters.NumberFilter(
        field_name="ppf2024",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total. Menor que."))
    ppf2024_gt = django_filters.NumberFilter(
        field_name="ppf2024",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total. Mayor que."))
    ppf2024_lte = django_filters.NumberFilter(
        field_name="ppf2024",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total. Menor o igual que."))
    ppf2024_gte = django_filters.NumberFilter(
        field_name="ppf2024",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total. Mayor o igual que."))
    pt2024 = django_filters.NumberFilter(
        help_text=(
            "Población total de 20 a 24 años"))
    pt2024_lt = django_filters.NumberFilter(
        field_name="pt2024",
        lookup_expr="lt",
        help_text=(
            "Población total de 20 a 24 años. Menor que."))
    pt2024_gt = django_filters.NumberFilter(
        field_name="pt2024",
        lookup_expr="gt",
        help_text=(
            "Población total de 20 a 24 años. Mayor que."))
    pt2024_lte = django_filters.NumberFilter(
        field_name="pt2024",
        lookup_expr="lte",
        help_text=(
            "Población total de 20 a 24 años. Menor o igual que."))
    pt2024_gte = django_filters.NumberFilter(
        field_name="pt2024",
        lookup_expr="gte",
        help_text=(
            "Población total de 20 a 24 años. Mayor o igual que."))
    ppt2024 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total"))
    ppt2024_lt = django_filters.NumberFilter(
        field_name="ppt2024",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total. Menor que."))
    ppt2024_gt = django_filters.NumberFilter(
        field_name="ppt2024",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total. Mayor que."))
    ppt2024_lte = django_filters.NumberFilter(
        field_name="ppt2024",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total. Menor o igual que."))
    ppt2024_gte = django_filters.NumberFilter(
        field_name="ppt2024",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total. Mayor o igual que."))
    pm2529 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 25 a 29 años"))
    pm2529_lt = django_filters.NumberFilter(
        field_name="pm2529",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 25 a 29 años. Menor que."))
    pm2529_gt = django_filters.NumberFilter(
        field_name="pm2529",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 25 a 29 años. Mayor que."))
    pm2529_lte = django_filters.NumberFilter(
        field_name="pm2529",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 25 a 29 años. Menor o igual que."))
    pm2529_gte = django_filters.NumberFilter(
        field_name="pm2529",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 25 a 29 años. Mayor o igual que."))
    ppm2529 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total"))
    ppm2529_lt = django_filters.NumberFilter(
        field_name="ppm2529",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total. Menor que."))
    ppm2529_gt = django_filters.NumberFilter(
        field_name="ppm2529",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total. Mayor que."))
    ppm2529_lte = django_filters.NumberFilter(
        field_name="ppm2529",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total. Menor o igual que."))
    ppm2529_gte = django_filters.NumberFilter(
        field_name="ppm2529",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total. Mayor o igual que."))
    pf2529 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 25 a 29 años"))
    pf2529_lt = django_filters.NumberFilter(
        field_name="pf2529",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 25 a 29 años. Menor que."))
    pf2529_gt = django_filters.NumberFilter(
        field_name="pf2529",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 25 a 29 años. Mayor que."))
    pf2529_lte = django_filters.NumberFilter(
        field_name="pf2529",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 25 a 29 años. Menor o igual que."))
    pf2529_gte = django_filters.NumberFilter(
        field_name="pf2529",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 25 a 29 años. Mayor o igual que."))
    ppf2529 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total"))
    ppf2529_lt = django_filters.NumberFilter(
        field_name="ppf2529",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total. Menor que."))
    ppf2529_gt = django_filters.NumberFilter(
        field_name="ppf2529",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total. Mayor que."))
    ppf2529_lte = django_filters.NumberFilter(
        field_name="ppf2529",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total. Menor o igual que."))
    ppf2529_gte = django_filters.NumberFilter(
        field_name="ppf2529",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total. Mayor o igual que."))
    pt2529 = django_filters.NumberFilter(
        help_text=(
            "Población total de 25 a 29 años"))
    pt2529_lt = django_filters.NumberFilter(
        field_name="pt2529",
        lookup_expr="lt",
        help_text=(
            "Población total de 25 a 29 años. Menor que."))
    pt2529_gt = django_filters.NumberFilter(
        field_name="pt2529",
        lookup_expr="gt",
        help_text=(
            "Población total de 25 a 29 años. Mayor que."))
    pt2529_lte = django_filters.NumberFilter(
        field_name="pt2529",
        lookup_expr="lte",
        help_text=(
            "Población total de 25 a 29 años. Menor o igual que."))
    pt2529_gte = django_filters.NumberFilter(
        field_name="pt2529",
        lookup_expr="gte",
        help_text=(
            "Población total de 25 a 29 años. Mayor o igual que."))
    ppt2529 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total"))
    ppt2529_lt = django_filters.NumberFilter(
        field_name="ppt2529",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total. Menor que."))
    ppt2529_gt = django_filters.NumberFilter(
        field_name="ppt2529",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total. Mayor que."))
    ppt2529_lte = django_filters.NumberFilter(
        field_name="ppt2529",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total. Menor o igual que."))
    ppt2529_gte = django_filters.NumberFilter(
        field_name="ppt2529",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total. Mayor o igual que."))
    pm3034 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 30 a 34 años"))
    pm3034_lt = django_filters.NumberFilter(
        field_name="pm3034",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 30 a 34 años. Menor que."))
    pm3034_gt = django_filters.NumberFilter(
        field_name="pm3034",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 30 a 34 años. Mayor que."))
    pm3034_lte = django_filters.NumberFilter(
        field_name="pm3034",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 30 a 34 años. Menor o igual que."))
    pm3034_gte = django_filters.NumberFilter(
        field_name="pm3034",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 30 a 34 años. Mayor o igual que."))
    ppm3034 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total"))
    ppm3034_lt = django_filters.NumberFilter(
        field_name="ppm3034",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total. Menor que."))
    ppm3034_gt = django_filters.NumberFilter(
        field_name="ppm3034",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total. Mayor que."))
    ppm3034_lte = django_filters.NumberFilter(
        field_name="ppm3034",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total. Menor o igual que."))
    ppm3034_gte = django_filters.NumberFilter(
        field_name="ppm3034",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total. Mayor o igual que."))
    pf3034 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 30 a 34 años"))
    pf3034_lt = django_filters.NumberFilter(
        field_name="pf3034",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 30 a 34 años. Menor que."))
    pf3034_gt = django_filters.NumberFilter(
        field_name="pf3034",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 30 a 34 años. Mayor que."))
    pf3034_lte = django_filters.NumberFilter(
        field_name="pf3034",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 30 a 34 años. Menor o igual que."))
    pf3034_gte = django_filters.NumberFilter(
        field_name="pf3034",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 30 a 34 años. Mayor o igual que."))
    ppf3034 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total"))
    ppf3034_lt = django_filters.NumberFilter(
        field_name="ppf3034",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total. Menor que."))
    ppf3034_gt = django_filters.NumberFilter(
        field_name="ppf3034",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total. Mayor que."))
    ppf3034_lte = django_filters.NumberFilter(
        field_name="ppf3034",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total. Menor o igual que."))
    ppf3034_gte = django_filters.NumberFilter(
        field_name="ppf3034",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total. Mayor o igual que."))
    pt3034 = django_filters.NumberFilter(
        help_text=(
            "Población total de 30 a 34 años"))
    pt3034_lt = django_filters.NumberFilter(
        field_name="pt3034",
        lookup_expr="lt",
        help_text=(
            "Población total de 30 a 34 años. Menor que."))
    pt3034_gt = django_filters.NumberFilter(
        field_name="pt3034",
        lookup_expr="gt",
        help_text=(
            "Población total de 30 a 34 años. Mayor que."))
    pt3034_lte = django_filters.NumberFilter(
        field_name="pt3034",
        lookup_expr="lte",
        help_text=(
            "Población total de 30 a 34 años. Menor o igual que."))
    pt3034_gte = django_filters.NumberFilter(
        field_name="pt3034",
        lookup_expr="gte",
        help_text=(
            "Población total de 30 a 34 años. Mayor o igual que."))
    ppt3034 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total"))
    ppt3034_lt = django_filters.NumberFilter(
        field_name="ppt3034",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total. Menor que."))
    ppt3034_gt = django_filters.NumberFilter(
        field_name="ppt3034",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total. Mayor que."))
    ppt3034_lte = django_filters.NumberFilter(
        field_name="ppt3034",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total. Menor o igual que."))
    ppt3034_gte = django_filters.NumberFilter(
        field_name="ppt3034",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total. Mayor o igual que."))
    pm3539 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 35 a 39 años"))
    pm3539_lt = django_filters.NumberFilter(
        field_name="pm3539",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 35 a 39 años. Menor que."))
    pm3539_gt = django_filters.NumberFilter(
        field_name="pm3539",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 35 a 39 años. Mayor que."))
    pm3539_lte = django_filters.NumberFilter(
        field_name="pm3539",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 35 a 39 años. Menor o igual que."))
    pm3539_gte = django_filters.NumberFilter(
        field_name="pm3539",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 35 a 39 años. Mayor o igual que."))
    ppm3539 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total"))
    ppm3539_lt = django_filters.NumberFilter(
        field_name="ppm3539",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total. Menor que."))
    ppm3539_gt = django_filters.NumberFilter(
        field_name="ppm3539",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total. Mayor que."))
    ppm3539_lte = django_filters.NumberFilter(
        field_name="ppm3539",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total. Menor o igual que."))
    ppm3539_gte = django_filters.NumberFilter(
        field_name="ppm3539",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total. Mayor o igual que."))
    pf3539 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 35 a 39 años"))
    pf3539_lt = django_filters.NumberFilter(
        field_name="pf3539",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 35 a 39 años. Menor que."))
    pf3539_gt = django_filters.NumberFilter(
        field_name="pf3539",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 35 a 39 años. Mayor que."))
    pf3539_lte = django_filters.NumberFilter(
        field_name="pf3539",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 35 a 39 años. Menor o igual que."))
    pf3539_gte = django_filters.NumberFilter(
        field_name="pf3539",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 35 a 39 años. Mayor o igual que."))
    ppf3539 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total"))
    ppf3539_lt = django_filters.NumberFilter(
        field_name="ppf3539",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total. Menor que."))
    ppf3539_gt = django_filters.NumberFilter(
        field_name="ppf3539",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total. Mayor que."))
    ppf3539_lte = django_filters.NumberFilter(
        field_name="ppf3539",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total. Menor o igual que."))
    ppf3539_gte = django_filters.NumberFilter(
        field_name="ppf3539",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total. Mayor o igual que."))
    pt3539 = django_filters.NumberFilter(
        help_text=(
            "Población total de 35 a 39 años"))
    pt3539_lt = django_filters.NumberFilter(
        field_name="pt3539",
        lookup_expr="lt",
        help_text=(
            "Población total de 35 a 39 años. Menor que."))
    pt3539_gt = django_filters.NumberFilter(
        field_name="pt3539",
        lookup_expr="gt",
        help_text=(
            "Población total de 35 a 39 años. Mayor que."))
    pt3539_lte = django_filters.NumberFilter(
        field_name="pt3539",
        lookup_expr="lte",
        help_text=(
            "Población total de 35 a 39 años. Menor o igual que."))
    pt3539_gte = django_filters.NumberFilter(
        field_name="pt3539",
        lookup_expr="gte",
        help_text=(
            "Población total de 35 a 39 años. Mayor o igual que."))
    ppt3539 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total"))
    ppt3539_lt = django_filters.NumberFilter(
        field_name="ppt3539",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total. Menor que."))
    ppt3539_gt = django_filters.NumberFilter(
        field_name="ppt3539",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total. Mayor que."))
    ppt3539_lte = django_filters.NumberFilter(
        field_name="ppt3539",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total. Menor o igual que."))
    ppt3539_gte = django_filters.NumberFilter(
        field_name="ppt3539",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total. Mayor o igual que."))
    pm4044 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 40 a 44 años"))
    pm4044_lt = django_filters.NumberFilter(
        field_name="pm4044",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 40 a 44 años. Menor que."))
    pm4044_gt = django_filters.NumberFilter(
        field_name="pm4044",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 40 a 44 años. Mayor que."))
    pm4044_lte = django_filters.NumberFilter(
        field_name="pm4044",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 40 a 44 años. Menor o igual que."))
    pm4044_gte = django_filters.NumberFilter(
        field_name="pm4044",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 40 a 44 años. Mayor o igual que."))
    ppm4044 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total"))
    ppm4044_lt = django_filters.NumberFilter(
        field_name="ppm4044",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total. Menor que."))
    ppm4044_gt = django_filters.NumberFilter(
        field_name="ppm4044",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total. Mayor que."))
    ppm4044_lte = django_filters.NumberFilter(
        field_name="ppm4044",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total. Menor o igual que."))
    ppm4044_gte = django_filters.NumberFilter(
        field_name="ppm4044",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total. Mayor o igual que."))
    pf4044 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 40 a 44 años"))
    pf4044_lt = django_filters.NumberFilter(
        field_name="pf4044",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 40 a 44 años. Menor que."))
    pf4044_gt = django_filters.NumberFilter(
        field_name="pf4044",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 40 a 44 años. Mayor que."))
    pf4044_lte = django_filters.NumberFilter(
        field_name="pf4044",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 40 a 44 años. Menor o igual que."))
    pf4044_gte = django_filters.NumberFilter(
        field_name="pf4044",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 40 a 44 años. Mayor o igual que."))
    ppf4044 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total"))
    ppf4044_lt = django_filters.NumberFilter(
        field_name="ppf4044",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total. Menor que."))
    ppf4044_gt = django_filters.NumberFilter(
        field_name="ppf4044",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total. Mayor que."))
    ppf4044_lte = django_filters.NumberFilter(
        field_name="ppf4044",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total. Menor o igual que."))
    ppf4044_gte = django_filters.NumberFilter(
        field_name="ppf4044",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total. Mayor o igual que."))
    pt4044 = django_filters.NumberFilter(
        help_text=(
            "Población total de 40 a 44 años"))
    pt4044_lt = django_filters.NumberFilter(
        field_name="pt4044",
        lookup_expr="lt",
        help_text=(
            "Población total de 40 a 44 años. Menor que."))
    pt4044_gt = django_filters.NumberFilter(
        field_name="pt4044",
        lookup_expr="gt",
        help_text=(
            "Población total de 40 a 44 años. Mayor que."))
    pt4044_lte = django_filters.NumberFilter(
        field_name="pt4044",
        lookup_expr="lte",
        help_text=(
            "Población total de 40 a 44 años. Menor o igual que."))
    pt4044_gte = django_filters.NumberFilter(
        field_name="pt4044",
        lookup_expr="gte",
        help_text=(
            "Población total de 40 a 44 años. Mayor o igual que."))
    ppt4044 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total"))
    ppt4044_lt = django_filters.NumberFilter(
        field_name="ppt4044",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total. Menor que."))
    ppt4044_gt = django_filters.NumberFilter(
        field_name="ppt4044",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total. Mayor que."))
    ppt4044_lte = django_filters.NumberFilter(
        field_name="ppt4044",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total. Menor o igual que."))
    ppt4044_gte = django_filters.NumberFilter(
        field_name="ppt4044",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total. Mayor o igual que."))
    pm4549 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 45 a 49 años"))
    pm4549_lt = django_filters.NumberFilter(
        field_name="pm4549",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 45 a 49 años. Menor que."))
    pm4549_gt = django_filters.NumberFilter(
        field_name="pm4549",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 45 a 49 años. Mayor que."))
    pm4549_lte = django_filters.NumberFilter(
        field_name="pm4549",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 45 a 49 años. Menor o igual que."))
    pm4549_gte = django_filters.NumberFilter(
        field_name="pm4549",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 45 a 49 años. Mayor o igual que."))
    ppm4549 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total"))
    ppm4549_lt = django_filters.NumberFilter(
        field_name="ppm4549",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total. Menor que."))
    ppm4549_gt = django_filters.NumberFilter(
        field_name="ppm4549",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total. Mayor que."))
    ppm4549_lte = django_filters.NumberFilter(
        field_name="ppm4549",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total. Menor o igual que."))
    ppm4549_gte = django_filters.NumberFilter(
        field_name="ppm4549",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total. Mayor o igual que."))
    pf4549 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 45 a 49 años"))
    pf4549_lt = django_filters.NumberFilter(
        field_name="pf4549",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 45 a 49 años. Menor que."))
    pf4549_gt = django_filters.NumberFilter(
        field_name="pf4549",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 45 a 49 años. Mayor que."))
    pf4549_lte = django_filters.NumberFilter(
        field_name="pf4549",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 45 a 49 años. Menor o igual que."))
    pf4549_gte = django_filters.NumberFilter(
        field_name="pf4549",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 45 a 49 años. Mayor o igual que."))
    ppf4549 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total"))
    ppf4549_lt = django_filters.NumberFilter(
        field_name="ppf4549",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total. Menor que."))
    ppf4549_gt = django_filters.NumberFilter(
        field_name="ppf4549",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total. Mayor que."))
    ppf4549_lte = django_filters.NumberFilter(
        field_name="ppf4549",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total. Menor o igual que."))
    ppf4549_gte = django_filters.NumberFilter(
        field_name="ppf4549",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total. Mayor o igual que."))
    pt4549 = django_filters.NumberFilter(
        help_text=(
            "Población total de 45 a 49 años"))
    pt4549_lt = django_filters.NumberFilter(
        field_name="pt4549",
        lookup_expr="lt",
        help_text=(
            "Población total de 45 a 49 años. Menor que."))
    pt4549_gt = django_filters.NumberFilter(
        field_name="pt4549",
        lookup_expr="gt",
        help_text=(
            "Población total de 45 a 49 años. Mayor que."))
    pt4549_lte = django_filters.NumberFilter(
        field_name="pt4549",
        lookup_expr="lte",
        help_text=(
            "Población total de 45 a 49 años. Menor o igual que."))
    pt4549_gte = django_filters.NumberFilter(
        field_name="pt4549",
        lookup_expr="gte",
        help_text=(
            "Población total de 45 a 49 años. Mayor o igual que."))
    ppt4549 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total"))
    ppt4549_lt = django_filters.NumberFilter(
        field_name="ppt4549",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total. Menor que."))
    ppt4549_gt = django_filters.NumberFilter(
        field_name="ppt4549",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total. Mayor que."))
    ppt4549_lte = django_filters.NumberFilter(
        field_name="ppt4549",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total. Menor o igual que."))
    ppt4549_gte = django_filters.NumberFilter(
        field_name="ppt4549",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total. Mayor o igual que."))
    pm5054 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 50 a 54 años"))
    pm5054_lt = django_filters.NumberFilter(
        field_name="pm5054",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 50 a 54 años. Menor que."))
    pm5054_gt = django_filters.NumberFilter(
        field_name="pm5054",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 50 a 54 años. Mayor que."))
    pm5054_lte = django_filters.NumberFilter(
        field_name="pm5054",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 50 a 54 años. Menor o igual que."))
    pm5054_gte = django_filters.NumberFilter(
        field_name="pm5054",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 50 a 54 años. Mayor o igual que."))
    ppm5054 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total"))
    ppm5054_lt = django_filters.NumberFilter(
        field_name="ppm5054",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total. Menor que."))
    ppm5054_gt = django_filters.NumberFilter(
        field_name="ppm5054",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total. Mayor que."))
    ppm5054_lte = django_filters.NumberFilter(
        field_name="ppm5054",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total. Menor o igual que."))
    ppm5054_gte = django_filters.NumberFilter(
        field_name="ppm5054",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total. Mayor o igual que."))
    pf5054 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 50 a 54 años"))
    pf5054_lt = django_filters.NumberFilter(
        field_name="pf5054",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 50 a 54 años. Menor que."))
    pf5054_gt = django_filters.NumberFilter(
        field_name="pf5054",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 50 a 54 años. Mayor que."))
    pf5054_lte = django_filters.NumberFilter(
        field_name="pf5054",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 50 a 54 años. Menor o igual que."))
    pf5054_gte = django_filters.NumberFilter(
        field_name="pf5054",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 50 a 54 años. Mayor o igual que."))
    ppf5054 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total"))
    ppf5054_lt = django_filters.NumberFilter(
        field_name="ppf5054",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total. Menor que."))
    ppf5054_gt = django_filters.NumberFilter(
        field_name="ppf5054",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total. Mayor que."))
    ppf5054_lte = django_filters.NumberFilter(
        field_name="ppf5054",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total. Menor o igual que."))
    ppf5054_gte = django_filters.NumberFilter(
        field_name="ppf5054",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total. Mayor o igual que."))
    pt5054 = django_filters.NumberFilter(
        help_text=(
            "Población total de 50 a 54 años"))
    pt5054_lt = django_filters.NumberFilter(
        field_name="pt5054",
        lookup_expr="lt",
        help_text=(
            "Población total de 50 a 54 años. Menor que."))
    pt5054_gt = django_filters.NumberFilter(
        field_name="pt5054",
        lookup_expr="gt",
        help_text=(
            "Población total de 50 a 54 años. Mayor que."))
    pt5054_lte = django_filters.NumberFilter(
        field_name="pt5054",
        lookup_expr="lte",
        help_text=(
            "Población total de 50 a 54 años. Menor o igual que."))
    pt5054_gte = django_filters.NumberFilter(
        field_name="pt5054",
        lookup_expr="gte",
        help_text=(
            "Población total de 50 a 54 años. Mayor o igual que."))
    ppt5054 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total"))
    ppt5054_lt = django_filters.NumberFilter(
        field_name="ppt5054",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total. Menor que."))
    ppt5054_gt = django_filters.NumberFilter(
        field_name="ppt5054",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total. Mayor que."))
    ppt5054_lte = django_filters.NumberFilter(
        field_name="ppt5054",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total. Menor o igual que."))
    ppt5054_gte = django_filters.NumberFilter(
        field_name="ppt5054",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total. Mayor o igual que."))
    pm5559 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 55 a 59 años"))
    pm5559_lt = django_filters.NumberFilter(
        field_name="pm5559",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 55 a 59 años. Menor que."))
    pm5559_gt = django_filters.NumberFilter(
        field_name="pm5559",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 55 a 59 años. Mayor que."))
    pm5559_lte = django_filters.NumberFilter(
        field_name="pm5559",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 55 a 59 años. Menor o igual que."))
    pm5559_gte = django_filters.NumberFilter(
        field_name="pm5559",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 55 a 59 años. Mayor o igual que."))
    ppm5559 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total"))
    ppm5559_lt = django_filters.NumberFilter(
        field_name="ppm5559",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total. Menor que."))
    ppm5559_gt = django_filters.NumberFilter(
        field_name="ppm5559",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total. Mayor que."))
    ppm5559_lte = django_filters.NumberFilter(
        field_name="ppm5559",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total. Menor o igual que."))
    ppm5559_gte = django_filters.NumberFilter(
        field_name="ppm5559",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total. Mayor o igual que."))
    pf5559 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 55 a 59 años"))
    pf5559_lt = django_filters.NumberFilter(
        field_name="pf5559",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 55 a 59 años. Menor que."))
    pf5559_gt = django_filters.NumberFilter(
        field_name="pf5559",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 55 a 59 años. Mayor que."))
    pf5559_lte = django_filters.NumberFilter(
        field_name="pf5559",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 55 a 59 años. Menor o igual que."))
    pf5559_gte = django_filters.NumberFilter(
        field_name="pf5559",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 55 a 59 años. Mayor o igual que."))
    ppf5559 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total"))
    ppf5559_lt = django_filters.NumberFilter(
        field_name="ppf5559",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total. Menor que."))
    ppf5559_gt = django_filters.NumberFilter(
        field_name="ppf5559",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total. Mayor que."))
    ppf5559_lte = django_filters.NumberFilter(
        field_name="ppf5559",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total. Menor o igual que."))
    ppf5559_gte = django_filters.NumberFilter(
        field_name="ppf5559",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total. Mayor o igual que."))
    pt5559 = django_filters.NumberFilter(
        help_text=(
            "Población total de 55 a 59 años"))
    pt5559_lt = django_filters.NumberFilter(
        field_name="pt5559",
        lookup_expr="lt",
        help_text=(
            "Población total de 55 a 59 años. Menor que."))
    pt5559_gt = django_filters.NumberFilter(
        field_name="pt5559",
        lookup_expr="gt",
        help_text=(
            "Población total de 55 a 59 años. Mayor que."))
    pt5559_lte = django_filters.NumberFilter(
        field_name="pt5559",
        lookup_expr="lte",
        help_text=(
            "Población total de 55 a 59 años. Menor o igual que."))
    pt5559_gte = django_filters.NumberFilter(
        field_name="pt5559",
        lookup_expr="gte",
        help_text=(
            "Población total de 55 a 59 años. Mayor o igual que."))
    ppt5559 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total"))
    ppt5559_lt = django_filters.NumberFilter(
        field_name="ppt5559",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total. Menor que."))
    ppt5559_gt = django_filters.NumberFilter(
        field_name="ppt5559",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total. Mayor que."))
    ppt5559_lte = django_filters.NumberFilter(
        field_name="ppt5559",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total. Menor o igual que."))
    ppt5559_gte = django_filters.NumberFilter(
        field_name="ppt5559",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total. Mayor o igual que."))
    pm6064 = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 60 a 64 años"))
    pm6064_lt = django_filters.NumberFilter(
        field_name="pm6064",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 60 a 64 años. Menor que."))
    pm6064_gt = django_filters.NumberFilter(
        field_name="pm6064",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 60 a 64 años. Mayor que."))
    pm6064_lte = django_filters.NumberFilter(
        field_name="pm6064",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 60 a 64 años. Menor o igual que."))
    pm6064_gte = django_filters.NumberFilter(
        field_name="pm6064",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 60 a 64 años. Mayor o igual que."))
    ppm6064 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total"))
    ppm6064_lt = django_filters.NumberFilter(
        field_name="ppm6064",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total. Menor que."))
    ppm6064_gt = django_filters.NumberFilter(
        field_name="ppm6064",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total. Mayor que."))
    ppm6064_lte = django_filters.NumberFilter(
        field_name="ppm6064",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total. Menor o igual que."))
    ppm6064_gte = django_filters.NumberFilter(
        field_name="ppm6064",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total. Mayor o igual que."))
    pf6064 = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 60 a 64 años"))
    pf6064_lt = django_filters.NumberFilter(
        field_name="pf6064",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 60 a 64 años. Menor que."))
    pf6064_gt = django_filters.NumberFilter(
        field_name="pf6064",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 60 a 64 años. Mayor que."))
    pf6064_lte = django_filters.NumberFilter(
        field_name="pf6064",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 60 a 64 años. Menor o igual que."))
    pf6064_gte = django_filters.NumberFilter(
        field_name="pf6064",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 60 a 64 años. Mayor o igual que."))
    ppf6064 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total"))
    ppf6064_lt = django_filters.NumberFilter(
        field_name="ppf6064",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total. Menor que."))
    ppf6064_gt = django_filters.NumberFilter(
        field_name="ppf6064",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total. Mayor que."))
    ppf6064_lte = django_filters.NumberFilter(
        field_name="ppf6064",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total. Menor o igual que."))
    ppf6064_gte = django_filters.NumberFilter(
        field_name="ppf6064",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total. Mayor o igual que."))
    pt6064 = django_filters.NumberFilter(
        help_text=(
            "Población total de 60 a 64 años"))
    pt6064_lt = django_filters.NumberFilter(
        field_name="pt6064",
        lookup_expr="lt",
        help_text=(
            "Población total de 60 a 64 años. Menor que."))
    pt6064_gt = django_filters.NumberFilter(
        field_name="pt6064",
        lookup_expr="gt",
        help_text=(
            "Población total de 60 a 64 años. Mayor que."))
    pt6064_lte = django_filters.NumberFilter(
        field_name="pt6064",
        lookup_expr="lte",
        help_text=(
            "Población total de 60 a 64 años. Menor o igual que."))
    pt6064_gte = django_filters.NumberFilter(
        field_name="pt6064",
        lookup_expr="gte",
        help_text=(
            "Población total de 60 a 64 años. Mayor o igual que."))
    ppt6064 = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total"))
    ppt6064_lt = django_filters.NumberFilter(
        field_name="ppt6064",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total. Menor que."))
    ppt6064_gt = django_filters.NumberFilter(
        field_name="ppt6064",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total. Mayor que."))
    ppt6064_lte = django_filters.NumberFilter(
        field_name="ppt6064",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total. Menor o igual que."))
    ppt6064_gte = django_filters.NumberFilter(
        field_name="ppt6064",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total. Mayor o igual que."))
    pm65ym = django_filters.NumberFilter(
        help_text=(
            "Población masculina de 65 años y más"))
    pm65ym_lt = django_filters.NumberFilter(
        field_name="pm65ym",
        lookup_expr="lt",
        help_text=(
            "Población masculina de 65 años y más. Menor que."))
    pm65ym_gt = django_filters.NumberFilter(
        field_name="pm65ym",
        lookup_expr="gt",
        help_text=(
            "Población masculina de 65 años y más. Mayor que."))
    pm65ym_lte = django_filters.NumberFilter(
        field_name="pm65ym",
        lookup_expr="lte",
        help_text=(
            "Población masculina de 65 años y más. Menor o igual que."))
    pm65ym_gte = django_filters.NumberFilter(
        field_name="pm65ym",
        lookup_expr="gte",
        help_text=(
            "Población masculina de 65 años y más. Mayor o igual que."))
    ppm65ym = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total"))
    ppm65ym_lt = django_filters.NumberFilter(
        field_name="ppm65ym",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total. Menor que."))
    ppm65ym_gt = django_filters.NumberFilter(
        field_name="ppm65ym",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total. Mayor que."))
    ppm65ym_lte = django_filters.NumberFilter(
        field_name="ppm65ym",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total. Menor o igual que."))
    ppm65ym_gte = django_filters.NumberFilter(
        field_name="ppm65ym",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total. Mayor o igual que."))
    pf65ym = django_filters.NumberFilter(
        help_text=(
            "Población femenina de 65 años y más"))
    pf65ym_lt = django_filters.NumberFilter(
        field_name="pf65ym",
        lookup_expr="lt",
        help_text=(
            "Población femenina de 65 años y más. Menor que."))
    pf65ym_gt = django_filters.NumberFilter(
        field_name="pf65ym",
        lookup_expr="gt",
        help_text=(
            "Población femenina de 65 años y más. Mayor que."))
    pf65ym_lte = django_filters.NumberFilter(
        field_name="pf65ym",
        lookup_expr="lte",
        help_text=(
            "Población femenina de 65 años y más. Menor o igual que."))
    pf65ym_gte = django_filters.NumberFilter(
        field_name="pf65ym",
        lookup_expr="gte",
        help_text=(
            "Población femenina de 65 años y más. Mayor o igual que."))
    ppf65ym = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total"))
    ppf65ym_lt = django_filters.NumberFilter(
        field_name="ppf65ym",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total. Menor que."))
    ppf65ym_gt = django_filters.NumberFilter(
        field_name="ppf65ym",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total. Mayor que."))
    ppf65ym_lte = django_filters.NumberFilter(
        field_name="ppf65ym",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total. Menor o igual que."))
    ppf65ym_gte = django_filters.NumberFilter(
        field_name="ppf65ym",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total. Mayor o igual que."))
    pt65ym = django_filters.NumberFilter(
        help_text=(
            "Población total de 65 años y más"))
    pt65ym_lt = django_filters.NumberFilter(
        field_name="pt65ym",
        lookup_expr="lt",
        help_text=(
            "Población total de 65 años y más. Menor que."))
    pt65ym_gt = django_filters.NumberFilter(
        field_name="pt65ym",
        lookup_expr="gt",
        help_text=(
            "Población total de 65 años y más. Mayor que."))
    pt65ym_lte = django_filters.NumberFilter(
        field_name="pt65ym",
        lookup_expr="lte",
        help_text=(
            "Población total de 65 años y más. Menor o igual que."))
    pt65ym_gte = django_filters.NumberFilter(
        field_name="pt65ym",
        lookup_expr="gte",
        help_text=(
            "Población total de 65 años y más. Mayor o igual que."))
    ppt65ym = django_filters.NumberFilter(
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total"))
    ppt65ym_lt = django_filters.NumberFilter(
        field_name="ppt65ym",
        lookup_expr="lt",
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total. Menor que."))
    ppt65ym_gt = django_filters.NumberFilter(
        field_name="ppt65ym",
        lookup_expr="gt",
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total. Mayor que."))
    ppt65ym_lte = django_filters.NumberFilter(
        field_name="ppt65ym",
        lookup_expr="lte",
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total. Menor o igual que."))
    ppt65ym_gte = django_filters.NumberFilter(
        field_name="ppt65ym",
        lookup_expr="gte",
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total. Mayor o igual que."))

    class Meta:
        model = MunicipioPoblacion
        fields = []
