import os
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from covid_update.descarga import descargar_datos
from covid_update.actualizar.casos import actualizar_casos


class Command(BaseCommand):
    help = 'Actualizar los casos de la base de datos de COVID'

    def add_arguments(self, parser):
        parser.add_argument(
            '--log',
            type=str,
            help='Ruta al archivo de log')
        parser.add_argument(
            '--verbose',
            action='store_true')
        parser.add_argument(
            '--no-descargar',
            action='store_true',
            help='Descargar los datos',
        )

    def handle(self, *args, **options):
        if not options['no_descargar']:
            descargar_datos()

        log = options.get('log', None)
        if log is None:
            directorio = os.path.join(
                settings.BASE_DIR,
                settings.DATOS_BASE_DIR,
                settings.LOGS_DIR)

            if not os.path.exists(directorio):
                os.makedirs(directorio)

            fecha = datetime.datetime.now().isoformat()
            log = os.path.join(directorio, f'{fecha}.log')

        if options['verbose']:
            log = None
        actualizar_casos(log=log)
