from django.db import models
from covid_data.models.base import ModeloBase


class Caso(ModeloBase):
    NO_ESPECIFICADO = 99

    renglon = models.IntegerField(
        help_text='Renglón en la tabla liberada más reciente.')
    id_registro = models.CharField(
        max_length=80,
        help_text='Identificador en la liberada más reciente.')
    fecha_actualizacion = models.DateField(
        help_text=(
            'La base de datos se alimenta diariamente, esta variable permite '
            'identificar la fecha de la ultima actualizacion.'),
        null=True)
    origen = models.ForeignKey(
        'Origen',
        on_delete=models.PROTECT,
        help_text=(
            'La vigilancia centinela se realiza a través del sistema de '
            'unidades de salud monitoras de enfermedades respiratorias '
            '(USMER). Las USMER incluyen unidades médicas del primer, segundo '
            'o tercer nivel de atención y también participan como USMER las '
            'unidades de tercer nivel que por sus características contribuyen '
            'a ampliar el panorama de información epidemiológica, entre ellas '
            'las que cuenten con especialidad de neumología, infectología o '
            'pediatría. (Categorías en Catalógo Anexo).'),
        null=True)
    sector = models.ForeignKey(
        'Sector',
        on_delete=models.PROTECT,
        help_text=(
            'Identifica el tipo de institución del Sistema Nacional de Salud '
            'que brindó la atención.'),
        null=True)
    entidad_um = models.ForeignKey(
        'Entidad',
        related_name='entidad_um',
        on_delete=models.PROTECT,
        help_text=(
            'Identifica la entidad donde se ubica la unidad medica que '
            'brindó la atención.'),
        null=True)
    sexo = models.ForeignKey(
        'Sexo',
        on_delete=models.PROTECT,
        help_text='Identifica al sexo del paciente.',
        null=True)
    entidad_nacimiento = models.ForeignKey(
        'Entidad',
        related_name='entidad_nacimiento',
        on_delete=models.PROTECT,
        help_text='Identifica la entidad de nacimiento del paciente.',
        null=True)
    entidad_residencia = models.ForeignKey(
        'Entidad',
        related_name='entidad_residencia',
        on_delete=models.PROTECT,
        help_text='Identifica la entidad de residencia del paciente.',
        null=True)
    municipio_residencia = models.ForeignKey(
        'Municipio',
        on_delete=models.PROTECT,
        help_text='Identifica el municipio de residencia del paciente.',
        null=True,)
    tipo_paciente = models.ForeignKey(
        'TipoPaciente',
        on_delete=models.PROTECT,
        help_text=(
            'Identifica el tipo de atención que recibió el paciente en la '
            'unidad. Se denomina como ambulatorio si regresó a su casa o se '
            'denomina como hospitalizado si fue ingresado a hospitalización.'),
        null=True)
    fecha_ingreso = models.DateField(
        help_text=(
            'Identifica la fecha de ingreso del paciente a la unidad '
            'de atención.'),
        null=True,)
    fecha_sintomas = models.DateField(
        help_text=(
            'Idenitifica la fecha en que inició la sintomatología '
            'del paciente.'),
        null=True)
    fecha_defuncion = models.DateField(
        help_text='Identifica la fecha en que el paciente falleció.',
        null=True)
    intubado = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='intubado',
        null=True,
        help_text='Identifica si el paciente requirió de intubación.')
    neumonia = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='neumonia',
        null=True,
        help_text='Identifica si al paciente se le diagnosticó con neumonía.')
    edad = models.IntegerField(help_text='Identifica la edad del paciente.')
    nacionalidad = models.ForeignKey(
        'Nacionalidad',
        on_delete=models.PROTECT,
        null=True,
        help_text='Identifica si el paciente es mexicano o extranjero.')
    embarazo = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='embarazo',
        null=True,
        help_text='Identifica si la paciente está embarazada.')
    habla_lengua_indigena = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='habla_lengua_indigena',
        null=True,
        help_text='Identifica si el paciente habla lengua índigena.')
    diabetes = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='diabetes',
        null=True,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico '
            'de diabetes.'))
    epoc = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='epoc',
        null=True,
        help_text='Identifica si el paciente tiene un diagnóstico de EPOC.')
    asma = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='asma',
        null=True,
        help_text='Identifica si el paciente tiene un diagnóstico de asma.')
    inmusupr = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='inmusupr',
        null=True,
        help_text='Identifica si el paciente presenta inmunosupresión.')
    hipertension = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='hipertension',
        null=True,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico '
            'de hipertensión.'))
    otras_com = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='otras_com',
        null=True,
        help_text=(
            'Identifica si el paciente tiene diagnóstico de '
            'otras enfermedades.'))
    cardiovascular = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='cardiovascular',
        null=True,
        help_text=(
            'Identifica si el paciente tiene un diagnóstico de '
            'enfermedades cardiovasculares.'))
    obesidad = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='obesidad',
        null=True,
        help_text='Identifica si el paciente tiene diagnóstico de obesidad.')
    renal_cronica = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='renal_cronica',
        null=True,
        help_text=(
            'Identifica si el paciente tiene diagnóstico de '
            'insuficiencia renal crónica.'))
    tabaquismo = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='tabaquismo',
        null=True,
        help_text='Identifica si el paciente tiene hábito de tabaquismo.')
    otro_caso = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='otro_caso',
        null=True,
        help_text=(
            'Identifica si el paciente tuvo contacto con algún otro '
            'caso diagnósticado con SARS CoV-2'))
    resultado = models.ForeignKey(
        'Resultado',
        null=True,
        on_delete=models.PROTECT,
        help_text=(
            'Identifica el resultado del análisis de la muestra reportado por '
            'el  laboratorio de la Red Nacional de Laboratorios de Vigilancia '
            'Epidemiológica (INDRE, LESP y LAVE). (Catálogo de resultados '
            'diagnósticos anexo).'
        ))
    migrante = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='migrante',
        null=True,
        help_text='Identifica si el paciente es una persona migrante.')
    pais_nacionalidad = models.ForeignKey(
        'Pais',
        related_name='pais_nacionalidad',
        null=True,
        on_delete=models.PROTECT,
        help_text='Identifica la nacionalidad del paciente.')
    pais_origen = models.ForeignKey(
        'Pais',
        related_name='pais_origen',
        null=True,
        on_delete=models.PROTECT,
        help_text=(
            'Identifica el país del que partió el paciente rumbo a '
            'México.'))
    uci = models.ForeignKey(
        'SiNo',
        on_delete=models.PROTECT,
        related_name='uci',
        null=True,
        help_text=(
            'Identifica si el paciente requirió ingresar a una Unidad de '
            'Cuidados Intensivos.'))
