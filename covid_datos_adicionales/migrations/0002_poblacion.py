import os
import pandas as pd
from django.db import transaction
from django.db import migrations


RUTA_POBLACION_XLS = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'data',
    'poblacion_municipios_2020.xlsx')


def cargar_poblacion(apps, schema_editor):
    Entidad = apps.get_model("covid_data", "Entidad")
    Municipio = apps.get_model("covid_data", "Municipio")
    EntidadPoblacion = apps.get_model("covid_datos_adicionales", "EntidadPoblacion")
    MunicipioPoblacion = apps.get_model("covid_datos_adicionales", "MunicipioPoblacion")

    datos = cargar_datos()

    with transaction.atomic():
        agregar_poblacion_entidades(datos, Entidad, EntidadPoblacion)
        agregar_poblacion_municipios(datos, Municipio, MunicipioPoblacion)


class Migration(migrations.Migration):

    dependencies = [
        ('covid_datos_adicionales', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_poblacion)
    ]


def cargar_datos():
    return pd.read_excel(RUTA_POBLACION_XLS)


def agregar_poblacion_entidades(datos, Entidad, EntidadPoblacion):
    datos_entidades = obtener_poblacion_por_entidades(datos)

    for entidad, renglon in datos_entidades.iterrows():
        defaults = {
            col.replace('-', ''): valor
            for col, valor in renglon.to_dict().items()}

        entidad = Entidad.objects.get(clave=entidad)
        _, creado = EntidadPoblacion.objects.get_or_create(
            entidad=entidad,
            defaults=defaults)

        if creado:
            print(f'Poblacion de entidad {entidad} registrada')


def agregar_poblacion_municipios(datos, Municipio, MunicipioPoblacion):
    columnas_poblacion = [col for col in datos.columns if col[0] == 'p']
    datos_municipios = datos[columnas_poblacion + ['agem']]
    for _, renglon in datos_municipios.iterrows():
        defaults = {
            col.replace('-', ''): valor
            for col, valor in renglon.to_dict().items()}

        clave_mun = int(defaults.pop('agem'))
        try:
            municipio = Municipio.objects.get(clave=clave_mun)
        except Municipio.DoesNotExist:
            print(f'Municipio faltante: {clave_mun}')
            continue

        _, creado = MunicipioPoblacion.objects.get_or_create(
            municipio=municipio,
            defaults=defaults)

        if creado:
            print(f'Poblacion de municipio {municipio} registrada')


def obtener_poblacion_por_entidades(df):
    # Extraer la clave de entidad de la clave geoestadística del municipio
    df['entidad'] = df['agem'].apply(lambda x: int(str(x)[:-3]))

    campos_poblacion = [
        x for x in df.columns if (x[0] == 'p') and (x[:2] != 'pp')]
    campos_porcentaje = [
        x for x in df.columns if x[:2] == 'pp']

    # Obtener sumas de poblacion por entidad
    pob_ent = df[campos_poblacion + ['entidad']].groupby('entidad').sum()

    # Calcular el porcentaje de población de cada grupo
    for col in campos_porcentaje:
        pob_ent[col] = pob_ent.apply(
            lambda x: 100 * x[col[1:]] / x['pt'],
            axis=1)

    return pob_ent
