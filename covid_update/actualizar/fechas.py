import re


FECHA_REGEX_1 = re.compile(r'([0-9]{2}\.[0-9]{2}\.[0-9]{4})')
FECHA_REGEX_2 = re.compile(r'(20[0-9]{2}[0-9]{2})')


def extraer_fecha_1(nombre):
    fecha = FECHA_REGEX_1.search(nombre).group(0)
    dia, mes, año = fecha.split('.')
    return f'{año}-{mes}-{dia}'


def extraer_fecha_2(nombre):
    fecha = FECHA_REGEX_2.search(nombre).group(0)
    año = '20' + fecha[:2]
    mes = fecha[2:4]
    dia = fecha[4:]
    return f'{año}-{mes}-{dia}'


PARSERS_FECHA = [
    extraer_fecha_1,
    extraer_fecha_2
]
