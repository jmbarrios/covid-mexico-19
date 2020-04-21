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
        if opciones['descargar']:
            mensaje = 'Descargando catalogos...'
            self.stdout.write(self.style.NOTICE(mensaje))
            descargar_catalogos(forzar=opciones['forzar'])

            mensaje = 'Procesando catalogos'
            self.stdout.write(self.style.NOTICE(mensaje))
            procesar_catalogos()

        mensaje = 'Actualizando catalogos'
        self.stdout.write(self.style.NOTICE(mensaje))
        actualizar_catalogos()

        mensaje = 'Catalogos actualizados exitosamente'
        self.stdout.write(self.style.SUCCESS(mensaje))
