import django_filters
from covid_data import models


VALORES_BOOLEANOS = (
    ('si', True),
    ('no', False)
)


class CasoFilter(django_filters.FilterSet):
    fecha_actualizacion = django_filters.DateFilter(
        help_text=(
            'Fecha de última actualización de la base '
            'de datos publicados. Búsqueda exacta.'))
    fecha_actualizacion_gt = django_filters.DateFilter(
        help_text=(
            'Fecha de última actualización de la base '
            'de datos publicados. Mayor que.'),
        field_name='fecha_actualizacion',
        lookup_expr='gt')
    fecha_actualizacion_lt = django_filters.DateFilter(
        help_text=(
            'Fecha de última actualización de la base '
            'de datos publicados. Menor que.'),
        field_name='fecha_actualizacion',
        lookup_expr='lt')
    fecha_actualizacion_gte = django_filters.DateFilter(
        help_text=(
            'Fecha de última actualización de la base '
            'de datos publicados. Mayor o igual que.'),
        field_name='fecha_actualizacion',
        lookup_expr='gte')
    fecha_actualizacion_lte = django_filters.DateFilter(
        help_text=(
            'Fecha de última actualización de la base '
            'de datos publicados. Menor  o igual que.'),
        field_name='fecha_actualizacion',
        lookup_expr='lte')

    fecha_ingreso = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad de '
            'atención. Búsqueda exacta.'))
    fecha_ingreso_gt = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad de '
            'atención. Mayor que.'),
        field_name='fecha_ingreso',
        lookup_expr='gt')
    fecha_ingreso_lt = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad de '
            'atención. Menor que.'),
        field_name='fecha_ingreso',
        lookup_expr='lt')
    fecha_ingreso_gte = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad de '
            'atención. Mayor o igual que.'),
        field_name='fecha_ingreso',
        lookup_expr='gte')
    fecha_ingreso_lte = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad de '
            'atención. Menor o igual que.'),
        field_name='fecha_ingreso',
        lookup_expr='lte')

    fecha_sintomas = django_filters.DateFilter(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología del '
            'paciente. Búsqueda exacta.'))
    fecha_sintomas_gt = django_filters.DateFilter(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología del '
            'paciente. Mayor que.'),
        field_name='fecha_sintomas',
        lookup_expr='gt')
    fecha_sintomas_lt = django_filters.DateFilter(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología del '
            'paciente. Menor que.'),
        field_name='fecha_sintomas',
        lookup_expr='lt')
    fecha_sintomas_gte = django_filters.DateFilter(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología del '
            'paciente. Mayor o igual que.'),
        field_name='fecha_sintomas',
        lookup_expr='gte')
    fecha_sintomas_lte = django_filters.DateFilter(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología del '
            'paciente. Menor o igual que.'),
        field_name='fecha_sintomas',
        lookup_expr='lte')

    fecha_defuncion = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha en que el paciente falleció. '
            'Búsqueda exacta.'))
    fecha_defuncion_gt = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha en que el paciente falleció. '
            'Mayor que.'),
        field_name='fecha_defuncion',
        lookup_expr='gt')
    fecha_defuncion_lt = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha en que el paciente falleció. '
            'Menor que.'),
        field_name='fecha_defuncion',
        lookup_expr='lt')
    fecha_defuncion_gte = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha en que el paciente falleció. '
            'Mayor o igual que.'),
        field_name='fecha_defuncion',
        lookup_expr='gte')
    fecha_defuncion_lte = django_filters.DateFilter(
        help_text=(
            'Identifica la fecha en que el paciente falleció. '
            'Menor o igual que.'),
        field_name='fecha_defuncion',
        lookup_expr='lte')
    defuncion = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        label='Defunción',
        help_text='Indentifica si el paciente falleció. si/no.',
        method='caso_defuncion')

    origen = django_filters.ModelChoiceFilter(
        queryset=models.Origen.objects.all(),
        help_text=(
            'Origen del reporte (USMER o fuera USMER). Búsqueda '
            'por ID.'))
    origen_clave = django_filters.NumberFilter(
        field_name='origen__clave',
        help_text=(
            'Origen del reporte (USMER o fuera USMER). Búsqueda '
            'por clave.'))
    origen_descripcion = django_filters.CharFilter(
        field_name='origen__descripcion',
        help_text=(
            'Origen del reporte (USMER o fuera USMER). Búsqueda '
            'exacta por descripción'))

    sector = django_filters.ModelChoiceFilter(
        queryset=models.Sector.objects.all(),
        help_text=(
            'Identifica el tipo de institución del Sistema Nacional de '
            'Salud que brindó la atención. Búsqueda por ID.'))
    sector_clave = django_filters.NumberFilter(
        field_name='sector__clave',
        help_text=(
            'Identifica el tipo de institución del Sistema Nacional de '
            'Salud que brindó la atención. Búsqueda por clave.'))
    sector_descripcion = django_filters.CharFilter(
        field_name='sector__descripcion',
        help_text=(
            'Identifica el tipo de institución del Sistema Nacional de '
            'Salud que brindó la atención. Búsqueda exacta por descripción.'))

    sexo = django_filters.ModelChoiceFilter(
        queryset=models.Sexo.objects.all(),
        help_text='Identifica al sexo del paciente. Búsqueda por ID.')
    sexo_clave = django_filters.NumberFilter(
        field_name='sexo__clave',
        help_text='Identifica al sexo del paciente. Búsqueda por clave.')
    sexo_descripcion = django_filters.CharFilter(
        field_name='sexo__descripcion',
        help_text=(
            'Identifica al sexo del paciente. Búsqueda exacta por '
            'descripción.'))

    tipo_paciente = django_filters.ModelChoiceFilter(
        queryset=models.TipoPaciente.objects.all(),
        help_text=(
            'Identifica el tipo de atención que recibió el paciente en '
            'la unidad. Búsqueda por ID.'))
    tipo_paciente_clave = django_filters.NumberFilter(
        field_name='tipo_paciente__clave',
        help_text=(
            'Identifica el tipo de atención que recibió el paciente en '
            'la unidad. Búsqueda por clave.'))
    tipo_paciente_descripcion = django_filters.CharFilter(
        field_name='tipo_paciente__descripcion',
        help_text=(
            'Identifica el tipo de atención que recibió el paciente en '
            'la unidad. Búsqueda exacta por descripción.'))

    nacionalidad = django_filters.ModelChoiceFilter(
        queryset=models.Nacionalidad.objects.all(),
        help_text=(
            'Identifica si el paciente es mexicano o extranjero. '
            'Búsqueda por ID.'))
    nacionalidad_clave = django_filters.NumberFilter(
        field_name='nacionalidad__clave',
        help_text=(
            'Identifica si el paciente es mexicano o extranjero. '
            'Búsqueda por clave.'))
    nacionalidad_descripcion = django_filters.CharFilter(
        field_name='nacionalidad__descripcion',
        help_text=(
            'Identifica si el paciente es mexicano o extranjero. '
            'Búsqueda exacta por descripción.'))

    edad = django_filters.NumberFilter(
        help_text='Identifica la edad del paciente. Búsqueda exacta.')
    edad_lt = django_filters.NumberFilter(
        field_name='edad',
        lookup_expr='lt',
        help_text='Identifica la edad del paciente. Mayor que.')
    edad_gt = django_filters.NumberFilter(
        field_name='edad',
        lookup_expr='gt',
        help_text='Identifica la edad del paciente. Menor que.')
    edad_lte = django_filters.NumberFilter(
        field_name='edad',
        lookup_expr='lte',
        help_text='Identifica la edad del paciente. Mayor o igual que.')
    edad_gte = django_filters.NumberFilter(
        field_name='edad',
        lookup_expr='gte',
        help_text='Identifica la edad del paciente. Menor o igual que.')

    positivo = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el resultado del análisis fue positivo. '
            'si/no.'),
        method='caso_positivo')
    negativo = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el resultado del análisis fue negativo. '
            'si/no.'),
        method='caso_negativo')
    pendiente = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el resultado del análisis está pendiente. '
            'si/no.'),
        method='caso_pendiente')

    intubado = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente requirió de intubación. '
            'si/no'),
        method='caso_intubado')
    intubado_clave = django_filters.NumberFilter(
        field_name='intubado__clave',
        help_text=(
            'Identifica si el paciente requirió de intubación. '
            'Búsqueda por clave.'))
    intubado_descripcion = django_filters.CharFilter(
        field_name='intubado__descripcion',
        help_text=(
            'Identifica si el paciente requirió de intubación. '
            'Búsqueda exacta por descripción.'))

    neumonia = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si al paciente se le diagnosticó con neumonía. '
            'si/no'),
        method='caso_neumonia')
    neumonia_clave = django_filters.NumberFilter(
        field_name='neumonia__clave',
        help_text=(
            'Identifica si al paciente se le diagnosticó con neumonía. '
            'Búsqueda por clave.'))
    neumonia_descripcion = django_filters.CharFilter(
        field_name='neumonia__descripcion',
        help_text=(
            'Identifica si al paciente se le diagnosticó con neumonía. '
            'Búsqueda exacta por descripción.'))

    embarazo = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text='Identifica si la paciente está embarazada. si/no.',
        method='caso_embarazo')
    embarazo_clave = django_filters.NumberFilter(
        field_name='embarazo__clave',
        help_text=(
            'Identifica si la paciente está embarazada. '
            'Búsqueda por clave.'))
    embarazo_descripcion = django_filters.CharFilter(
        field_name='embarazo__descripcion',
        help_text=(
            'Identifica si la paciente está embarazada. '
            'Búsqueda exacta por descripción.'))

    habla_lengua_indigena = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text='Identifica si el paciente habla lengua índigena. si/no.',
        method='caso_habla_lengua_indigena')
    habla_lengua_indigena_clave = django_filters.NumberFilter(
        field_name='habla_lengua_indigena__clave',
        help_text=(
            'Identifica si el paciente habla lengua índigena. '
            'Búsqueda por clave.'))
    habla_lengua_indigena_descripcion = django_filters.CharFilter(
        field_name='habla_lengua_indigena__descripcion',
        help_text=(
            'Identifica si el paciente habla lengua índigena. '
            'Búsqueda exacta por descripción.'))

    diabetes = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de diabetes. '
            'si/no.'),
        method='caso_diabetes')
    diabetes_clave = django_filters.NumberFilter(
        field_name='diabetes__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de diabetes. '
            'Búsqueda por clave.'))
    diabetes_descripcion = django_filters.CharFilter(
        field_name='diabetes__descripcion',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de diabetes. '
            'Búsqueda exacta por descripción.'))

    epoc = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de EPOC. '
            'si/no.'),
        method='caso_epoc')
    epoc_clave = django_filters.NumberFilter(
        field_name='epoc__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de EPOC. '
            'Búsqueda por clave.'))
    epoc_descripcion = django_filters.CharFilter(
        field_name='epoc__descripcion',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de EPOC. '
            'Búsqueda exacta por descripción.'))

    asma = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de asma. '
            'si/no.'),
        method='caso_asma')
    asma_clave = django_filters.NumberFilter(
        field_name='asma__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de asma. '
            'Búsqueda por clave.'))
    asma_descripcion = django_filters.CharFilter(
        field_name='asma__descripcion',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de asma. '
            'Búsqueda exacta por descripción.'))

    inmusupr = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente presenta inmunosupresión. '
            'si/no.'),
        method='caso_inmusupr')
    inmusupr_clave = django_filters.NumberFilter(
        field_name='inmusupr__clave',
        help_text=(
            'Identifica si el paciente presenta inmunosupresión. '
            'Búsqueda por clave.'))
    inmusupr_descripcion = django_filters.CharFilter(
        field_name='inmusupr__descripcion',
        help_text=(
            'Identifica si el paciente presenta inmunosupresión. '
            'Búsqueda exacta por descripción.'))

    hipertension = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de hipertensión. '
            'si/no.'),
        method='caso_hipertension')
    hipertension_clave = django_filters.NumberFilter(
        field_name='hipertension__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de hipertensión. '
            'Búsqueda por clave.'))
    hipertension_descripcion = django_filters.CharFilter(
        field_name='hipertension__descripcion',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de hipertensión. '
            'Búsqueda exacta por descripción.'))

    otras_com = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene diagnóstico de otras '
            'enfermedades. si/no.'),
        method='caso_otras_com')
    otras_com_clave = django_filters.NumberFilter(
        field_name='otras_com__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de otras '
            'enfermedades. Búsqueda por clave.'))
    otras_com_descripcion = django_filters.CharFilter(
        field_name='otras_com__descripcion',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de otras '
            'enfermedades. Búsqueda exacta por descripción.'))

    cardiovascular = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares. si/no.'),
        method='caso_cardiovascular')
    cardiovascular_clave = django_filters.NumberFilter(
        field_name='cardiovascular__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares. Búsqueda por clave.'))
    cardiovascular_descripcion = django_filters.CharFilter(
        field_name='cardiovascular__descripcion',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares. Búsqueda exacta por '
            'descripción.'))

    obesidad = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene diagnóstico de obesidad.'
            ' si/no.'),
        method='caso_obesidad')
    obesidad_clave = django_filters.NumberFilter(
        field_name='obesidad__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de obesidad. '
            'Búsqueda por clave.'))
    obesidad_descripcion = django_filters.CharFilter(
        field_name='obesidad__descripcion',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de obesidad. '
            'Búsqueda exacta por descripción.'))

    renal_cronica = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene diagnóstico de insuficiencia '
            'renal crónica. si/no.'),
        method='caso_renal_cronica')
    renal_cronica_clave = django_filters.NumberFilter(
        field_name='renal_cronica__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de insuficiencia '
            'renal crónica. Búsqueda por clave.'))
    renal_cronica_descripcion = django_filters.CharFilter(
        field_name='renal_cronica__descripcion',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de insuficiencia '
            'renal crónica. Búsqueda exacta por descripción.'))

    tabaquismo = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tiene hábito de tabaquismo. '
            'si/no.'),
        method='caso_tabaquismo')
    tabaquismo_clave = django_filters.NumberFilter(
        field_name='tabaquismo__clave',
        help_text=(
            'Identifica si el paciente tiene hábito de tabaquismo. '
            'Búsqueda por clave.'))
    tabaquismo_descripcion = django_filters.CharFilter(
        field_name='tabaquismo__descripcion',
        help_text=(
            'Identifica si el paciente tiene hábito de tabaquismo. '
            'Búsqueda exacta por descripción.'))

    otro_caso = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro caso '
            'diagnósticado con SARS CoV-2. si/no.'),
        method='caso_otro_caso')
    otro_caso_clave = django_filters.NumberFilter(
        field_name='otro_caso__clave',
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro caso '
            'diagnósticado con SARS CoV-2. Búsqueda por clave.'))
    otro_caso_descripcion = django_filters.CharFilter(
        field_name='otro_caso__descripcion',
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro caso '
            'diagnósticado con SARS CoV-2. Búsqueda exacta por descripción.'))

    migrante = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente es una persona migrante. '
            'si/no.'),
        method='caso_migrante')
    migrante_clave = django_filters.NumberFilter(
        field_name='migrante__clave',
        help_text=(
            'Identifica si el paciente es una persona migrante. '
            'Búsqueda por clave.'))
    migrante_descripcion = django_filters.CharFilter(
        field_name='migrante__descripcion',
        help_text=(
            'Identifica si el paciente es una persona migrante. '
            'Búsqueda exacta por descripción.'))

    uci = django_filters.ChoiceFilter(
        choices=VALORES_BOOLEANOS,
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad '
            'de Cuidados Intensivos. si/no.'),
        method='caso_uci')
    uci_clave = django_filters.NumberFilter(
        field_name='uci__clave',
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad '
            'de Cuidados Intensivos. Búsqueda por clave.'))
    uci_descripcion = django_filters.CharFilter(
        field_name='uci__descripcion',
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad '
            'de Cuidados Intensivos. Búsqueda exacta por descripción.'))

    entidades = models.Entidad.objects.all()

    entidad_um = django_filters.ModelChoiceFilter(
        queryset=entidades,
        help_text=(
            'Identifica la entidad donde se ubica la unidad medica que '
            'brindó la atención. Búsqueda por ID.'))
    entidad_um_clave = django_filters.NumberFilter(
        field_name='entidad_um__clave',
        help_text=(
            'Identifica la entidad donde se ubica la unidad medica que '
            'brindó la atención. Búsqueda por clave.'))
    entidad_um_descripcion = django_filters.CharFilter(
        field_name='entidad_um__descripcion',
        help_text=(
            'Identifica la entidad donde se ubica la unidad medica que '
            'brindó la atención. Búsqueda exacta por descripción.'))
    entidad_um_descripcion_contiene = django_filters.CharFilter(
        field_name='entidad_um__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica la entidad donde se ubica la unidad medica que '
            'brindó la atención. Búsqueda por descripción.'))

    entidad_nacimiento = django_filters.ModelChoiceFilter(
        queryset=entidades,
        help_text=(
            'Identifica la entidad de nacimiento del paciente.'
            ' Búsqueda por ID.'))
    entidad_nacimiento_clave = django_filters.NumberFilter(
        field_name='entidad_nacimiento__clave',
        help_text=(
            'Identifica la entidad de nacimiento del paciente.'
            ' Búsqueda por clave.'))
    entidad_nacimiento_descripcion = django_filters.CharFilter(
        field_name='entidad_nacimiento__descripcion',
        help_text=(
            'Identifica la entidad de nacimiento del paciente.'
            ' Búsqueda exacta por descripción.'))
    entidad_nacimiento_descripcion_contiene = django_filters.CharFilter(
        field_name='entidad_nacimiento__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica la entidad de nacimiento del paciente. '
            'Búsqueda por descripción.'))

    entidad_residencia = django_filters.ModelChoiceFilter(
        queryset=entidades,
        help_text=(
            'Identifica la entidad de residencia del paciente. '
            'Búsqueda por ID.'))
    entidad_residencia_clave = django_filters.NumberFilter(
        field_name='entidad_residencia__clave',
        help_text=(
            'Identifica la entidad de residencia del paciente. '
            'Búsqueda por clave.'))
    entidad_residencia_descripcion = django_filters.CharFilter(
        field_name='entidad_residencia__descripcion',
        help_text=(
            'Identifica la entidad de residencia del paciente. '
            'Búsqueda exacta por descripción.'))
    entidad_residencia_descripcion_contiene = django_filters.CharFilter(
        field_name='entidad_residencia__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica la entidad de residencia del paciente. '
            'Búsqueda por descripción.'))

    municipio_residencia_clave = django_filters.NumberFilter(
        field_name='municipio_residencia__clave',
        help_text=(
            'Identifica el municipio de residencia del paciente. '
            'Búsqueda por clave.'))
    municipio_residencia_descripcion = django_filters.CharFilter(
        field_name='municipio_residencia__descripcion',
        help_text=(
            'Identifica el municipio de residencia del paciente. '
            'Búsqueda exacta por descripción.'))
    municipio_residencia_descripcion_contiene = django_filters.CharFilter(
        field_name='municipio_residencia__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica el municipio de residencia del paciente. '
            'Búsqueda por descripción.'))

    pais_origen_clave = django_filters.NumberFilter(
        field_name='pais_origen__clave',
        help_text=(
            'Identifica el país del que partió el paciente rumbo a México. '
            'Búsqueda por clave.'))
    pais_origen_descripcion = django_filters.CharFilter(
        field_name='pais_origen__descripcion',
        help_text=(
            'Identifica el país del que partió el paciente rumbo a México. '
            'Búsqueda exacta por descripción.'))
    pais_origen_descripcion_contiene = django_filters.CharFilter(
        field_name='pais_origen__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica el país del que partió el paciente rumbo a México. '
            'Búsqueda por descripción.'))
    pais_origen_region = django_filters.CharFilter(
        field_name='pais_origen__region',
        lookup_expr='icontains',
        help_text=(
            'Identifica el país del que partió el paciente rumbo a México. '
            'Búsqueda por región. Se usó la regionalización del banco '
            'mundial.'))

    pais_nacionalidad_clave = django_filters.NumberFilter(
        field_name='pais_nacionalidad__clave',
        help_text=(
            'Identifica la nacionalidad del paciente. '
            'Búsqueda por clave.'))
    pais_nacionalidad_descripcion = django_filters.CharFilter(
        field_name='pais_nacionalidad__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica la nacionalidad del paciente. '
            'Búsqueda exacta por descripción.'))
    pais_nacionalidad_descripcion_contiene = django_filters.CharFilter(
        field_name='pais_nacionalidad__descripcion',
        lookup_expr='icontains',
        help_text=(
            'Identifica la nacionalidad del paciente. '
            'Búsqueda por descripción.'))
    pais_nacionalidad_region = django_filters.CharFilter(
        field_name='pais_nacionalidad__region',
        lookup_expr='icontains',
        help_text=(
            'Identifica la nacionalidad del paciente. '
            'Búsqueda por región. Se usó la regionalización del banco '
            'mundial.'))

    class Meta:
        model = models.Caso
        fields = []

    def caso_defuncion(self, queryset, name, value):
        return queryset.filter(fecha_defuncion__isnull=not value)

    def caso_positivo(self, queryset, name, value):
        return queryset.filter(resultado__clave=1)

    def caso_negativo(self, queryset, name, value):
        return queryset.filter(resultado__clave=2)

    def caso_pendiente(self, queryset, name, value):
        return queryset.filter(resultado__clave=3)

    def caso_intubado(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(intubado__clave=clave)

    def caso_neumonia(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(neumonia__clave=clave)

    def caso_embarazo(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(embarazo__clave=clave)

    def caso_habla_lengua_indigena(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(habla_lengua_indigena__clave=clave)

    def caso_diabetes(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(diabetes__clave=clave)

    def caso_epoc(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(epoc__clave=clave)

    def caso_asma(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(asma__clave=clave)

    def caso_inmusupr(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(inmusupr__clave=clave)

    def caso_hipertension(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(hipertension__clave=clave)

    def caso_otras_com(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(otras_com__clave=clave)

    def caso_cardiovascular(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(cardiovascular__clave=clave)

    def caso_obesidad(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(obesidad__clave=clave)

    def caso_renal_cronica(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(renal_cronica__clave=clave)

    def caso_tabaquismo(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(tabaquismo__clave=clave)

    def caso_otro_caso(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(otro_caso__clave=clave)

    def caso_migrate(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(migrate__clave=clave)

    def caso_uci(self, queryset, name, value):
        clave = 1 if value else 2
        return queryset.filter(uci__clave=clave)


COLUMNAS = {
    'fecha_actualizacion': 'fecha_actualizacion',
    'fecha_ingreso': 'fecha_ingreso',
    'fecha_sintomas': 'fecha_sintomas',
    'fecha_defuncion': 'fecha_defuncion',
    'edad': 'edad',
    'origen': 'origen__descripcion',
    'sector': 'sector__descripcion',
    'entidad_um': 'entidad_um__descripcion',
    'sexo': 'sexo__descripcion',
    'entidad_nacimiento': 'entidad_nacimiento__descripcion',
    'entidad_residencia': 'entidad_residencia__descripcion',
    'municipio_residencia': 'municipio_residencia__descripcion',
    'tipo_paciente': 'tipo_paciente__descripcion',
    'intubado': 'intubado__descripcion',
    'neumonia': 'neumonia__descripcion',
    'nacionalidad': 'nacionalidad__descripcion',
    'embarazo': 'embarazo__descripcion',
    'habla_lengua_indigena': 'habla_lengua_indigena__descripcion',
    'diabetes': 'diabetes__descripcion',
    'epoc': 'epoc__descripcion',
    'asma': 'asma__descripcion',
    'inmusupr': 'inmusupr__descripcion',
    'hipertension': 'hipertension__descripcion',
    'otras_com': 'otras_com__descripcion',
    'cardiovascular': 'cardiovascular__descripcion',
    'obesidad': 'obesidad__descripcion',
    'renal_cronica': 'renal_cronica__descripcion',
    'tabaquismo': 'tabaquismo__descripcion',
    'otro_caso': 'otro_caso__descripcion',
    'resultado': 'resultado__descripcion',
    'migrante': 'migrante__descripcion',
    'pais_nacionalidad': 'pais_nacionalidad__descripcion',
    'pais_origen': 'pais_origen__descripcion',
    'uci': 'uci__descripcion'
}


class CasoConteoFilter(CasoFilter):
    columna = django_filters.MultipleChoiceFilter(
        help_text='Columna sobre la cual se agrupan los casos.',
        choices=list(COLUMNAS.items()),
        method='agregar_por_columnas')

    class Meta:
        model = models.Caso
        fields = []

    def agregar_por_columnas(self, queryset, name, value):
        columnas = [COLUMNAS[col] for col in value]
        print(columnas)
        return queryset.values(*columnas)
