import django_filters
from covid_data import models


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
    defuncion = django_filters.BooleanFilter(
        label='Defunción',
        help_text='Indentifica si el paciente falleció. Si/No.',
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
        lookup_expr='icontains',
        help_text=(
            'Origen del reporte (USMER o fuera USMER). Búsqueda por '
            'descripción'))

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
        lookup_expr='icontains',
        help_text=(
            'Identifica el tipo de institución del Sistema Nacional de '
            'Salud que brindó la atención. Búsqueda por descripción.'))

    sexo = django_filters.ModelChoiceFilter(
        queryset=models.Sexo.objects.all(),
        help_text='Identifica al sexo del paciente. Búsqueda por ID.')
    sexo_clave = django_filters.NumberFilter(
        field_name='sexo__clave',
        help_text='Identifica al sexo del paciente. Búsqueda por clave.')
    sexo_descripcion = django_filters.CharFilter(
        field_name='sexo__descripcion',
        lookup_expr='icontains',
        help_text='Identifica al sexo del paciente. Búsqueda por descripción.')

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
        lookup_expr='icontains',
        help_text=(
            'Identifica el tipo de atención que recibió el paciente en '
            'la unidad. Búsqueda por descripción.'))

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
        lookup_expr='icontains',
        help_text=(
            'Identifica si el paciente es mexicano o extranjero. '
            'Búsqueda por descripción.'))

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

    positivo = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el resultado del análisis fue positivo. '
            'true/false.'),
        method='caso_positivo')
    negativo = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el resultado del análisis fue negativo. '
            'true/false.'),
        method='caso_negativo')
    pendiente = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el resultado del análisis está pendiente. '
            'true/false.'),
        method='caso_pendiente')

    intubado = django_filters.BooleanFilter(
        help_text='Identifica si el paciente requirió de intubación.',
        method='caso_intubado')
    intubado_clave = django_filters.NumberFilter(
        field_name='intubado__clave',
        help_text=(
            'Identifica si el paciente requirió de intubación. '
            'Búsqueda por clave.'))

    neumonia = django_filters.BooleanFilter(
        help_text='Identifica si al paciente se le diagnosticó con neumonía.',
        method='caso_neumonia')
    neumonia_clave = django_filters.NumberFilter(
        field_name='neumonia__clave',
        help_text=(
            'Identifica si al paciente se le diagnosticó con neumonía. '
            'Búsqueda por clave.'))

    embarazo = django_filters.BooleanFilter(
        help_text='Identifica si la paciente está embarazada.',
        method='caso_embarazo')
    embarazo_clave = django_filters.NumberFilter(
        field_name='embarazo__clave',
        help_text=(
            'Identifica si la paciente está embarazada. '
            'Búsqueda por clave.'))

    habla_lengua_indigena = django_filters.BooleanFilter(
        help_text='Identifica si el paciente habla lengua índigena.',
        method='caso_habla_lengua_indigena')
    habla_lengua_indigena_clave = django_filters.NumberFilter(
        field_name='habla_lengua_indigena__clave',
        help_text=(
            'Identifica si el paciente habla lengua índigena. '
            'Búsqueda por clave.'))

    diabetes = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de diabetes.'),
        method='caso_diabetes')
    diabetes_clave = django_filters.NumberFilter(
        field_name='diabetes__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de diabetes. '
            'Búsqueda por clave.'))

    epoc = django_filters.BooleanFilter(
        help_text='Identifica si el paciente tiene un diagnóstico de EPOC.',
        method='caso_epoc')
    epoc_clave = django_filters.NumberFilter(
        field_name='epoc__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de EPOC. '
            'Búsqueda por clave.'))

    asma = django_filters.BooleanFilter(
        help_text='Identifica si el paciente tiene un diagnóstico de asma.',
        method='caso_asma')
    asma_clave = django_filters.NumberFilter(
        field_name='asma__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de asma. '
            'Búsqueda por clave.'))

    asma = django_filters.BooleanFilter(
        help_text='Identifica si el paciente tiene un diagnóstico de asma.',
        method='caso_asma')
    asma_clave = django_filters.NumberFilter(
        field_name='asma__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de asma. '
            'Búsqueda por clave.'))

    inmusupr = django_filters.BooleanFilter(
        help_text='Identifica si el paciente presenta inmunosupresión.',
        method='caso_inmusupr')
    inmusupr_clave = django_filters.NumberFilter(
        field_name='inmusupr__clave',
        help_text=(
            'Identifica si el paciente presenta inmunosupresión. '
            'Búsqueda por clave.'))

    inmusupr = django_filters.BooleanFilter(
        help_text='Identifica si el paciente presenta inmunosupresión.',
        method='caso_inmusupr')
    inmusupr_clave = django_filters.NumberFilter(
        field_name='inmusupr__clave',
        help_text=(
            'Identifica si el paciente presenta inmunosupresión. '
            'Búsqueda por clave.'))

    hipertension = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de hipertensión.'),
        method='caso_hipertension')
    hipertension_clave = django_filters.NumberFilter(
        field_name='hipertension__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de hipertensión. '
            'Búsqueda por clave.'))

    otras_com = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene diagnóstico de otras '
            'enfermedades.'),
        method='caso_otras_com')
    otras_com_clave = django_filters.NumberFilter(
        field_name='otras_com__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de otras '
            'enfermedades. Búsqueda por clave.'))

    cardiovascular = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares. '),
        method='caso_cardiovascular')
    cardiovascular_clave = django_filters.NumberFilter(
        field_name='cardiovascular__clave',
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares. Búsqueda por clave.'))

    obesidad = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene diagnóstico de obesidad.'),
        method='caso_obesidad')
    obesidad_clave = django_filters.NumberFilter(
        field_name='obesidad__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de obesidad. '
            'Búsqueda por clave.'))

    renal_cronica = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene diagnóstico de insuficiencia '
            'renal crónica.'),
        method='caso_renal_cronica')
    renal_cronica_clave = django_filters.NumberFilter(
        field_name='renal_cronica__clave',
        help_text=(
            'Identifica si el paciente tiene diagnóstico de insuficiencia '
            'renal crónica. Búsqueda por clave.'))

    tabaquismo = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tiene hábito de tabaquismo.'),
        method='caso_tabaquismo')
    tabaquismo_clave = django_filters.NumberFilter(
        field_name='tabaquismo__clave',
        help_text=(
            'Identifica si el paciente tiene hábito de tabaquismo. '
            'Búsqueda por clave.'))

    otro_caso = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro caso '
            'diagnósticado con SARS CoV-2'),
        method='caso_otro_caso')
    otro_caso_clave = django_filters.NumberFilter(
        field_name='otro_caso__clave',
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro caso '
            'diagnósticado con SARS CoV-2. Búsqueda por clave.'))

    migrante = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente es una persona migrante.'),
        method='caso_migrante')
    migrante_clave = django_filters.NumberFilter(
        field_name='migrante__clave',
        help_text=(
            'Identifica si el paciente es una persona migrante. '
            'Búsqueda por clave.'))

    uci = django_filters.BooleanFilter(
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad '
            'de Cuidados Intensivos.'),
        method='caso_uci')
    uci_clave = django_filters.NumberFilter(
        field_name='uci__clave',
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad '
            'de Cuidados Intensivos. Búsqueda por clave.'))

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
        lookup_expr='icontains',
        help_text=(
            'Identifica la entidad de nacimiento del paciente.'
            ' Búsqueda por descripción.'))

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
