from django.core.management.base import BaseCommand

from covid_update.descarga import descargar_datos
from covid_update.actualizar.casos import actualizar_casos


class Command(BaseCommand):
    help = 'Actualizar los casos de la base de datos de COVID'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-descargar',
            action='store_true',
            help='Descargar los datos',
        )

    def handle(self, *args, **options):
        if not options['no_descargar']:
            descargar_datos()

        actualizar_casos()
