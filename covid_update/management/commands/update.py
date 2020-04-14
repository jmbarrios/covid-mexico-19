from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from covid_update.descarga import descargar_datos
from covid_update.descarga import descargar_catalogos
from covid_update.catalogos import procesar_catalogos
from covid_update.actualizar_catalogos import actualizar_catalogos


class Command(BaseCommand):
    help = 'Actualizar la base de datos de COVID con casos nuevos'

    def handle(self, *args, **options):
        descargar_catalogos()
        procesar_catalogos()
        actualizar_catalogos()
