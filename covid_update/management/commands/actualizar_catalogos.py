from django.core.management.base import BaseCommand

from covid_update.descarga import descargar_catalogos
from covid_update.catalogos import procesar_catalogos
from covid_update.actualizar.catalogos import actualizar_catalogos


class Command(BaseCommand):
    help = 'Actualizar los catalogos de la base de datos de COVID'

    def add_arguments(self, parser):
        parser.add_argument(
            '--descargar',
            action='store_true',
            help='Descargar los catalogos',
        )
        parser.add_argument(
            '--forzar',
            action='store_true',
            help='Sobree escribir los archivos de catalogos',
        )

    def handle(self, *args, **opciones):
        if not opciones['descargar']:
            descargar_catalogos(forzar=opciones['forzar'])

        procesar_catalogos()
        actualizar_catalogos()
