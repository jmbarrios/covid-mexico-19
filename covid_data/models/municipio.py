from django.db import models
from django.contrib.gis.db.models import MultiPolygonField
from django.utils.functional import cached_property

from covid_data.models.base import ModeloBase
from covid_data.models.caso import Caso


class Municipio(ModeloBase):
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=80)

    clave_municipio = models.IntegerField()
    entidad = models.ForeignKey(
        'Entidad',
        on_delete=models.CASCADE)
    geometria = MultiPolygonField()

    @cached_property
    def casos_confirmados(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            resultado__clave=1).count()

    @cached_property
    def casos_sospechosos(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            resultado__clave=3).count()

    @cached_property
    def casos_descartados(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            resultado__clave=2).count()

    @cached_property
    def defunciones_confirmadas(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            fecha_defuncion__isnull=False,
            resultado__clave=1).count()

    @cached_property
    def defunciones_sospechosas(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            fecha_defuncion__isnull=False,
            resultado__clave=3).count()

    @cached_property
    def intubados_confirmados(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            intubado__clave=1,
            resultado__clave=1).count()

    @cached_property
    def intubados_sospechosos(self):
        return (
            Caso.objects
            .filter(
                municipio_residencia=self,
                resultado__clave=3)
            .exclude(intubado__clave=1)
            .count())

    @cached_property
    def casos_hospitalizados(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            tipo_paciente__clave=2,
            resultado__clave=1).count()

    @cached_property
    def casos_hospitalizados_sospechosos(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            tipo_paciente__clave=2,
            resultado__clave=3).count()

    @cached_property
    def casos_ambulatorios(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            tipo_paciente__clave=1,
            resultado__clave=1).count()

    @cached_property
    def casos_ambulatorios_sospechosos(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            tipo_paciente__clave=1,
            resultado__clave=3).count()

    @cached_property
    def criticos_confirmados(self):
        return Caso.objects.filter(
            municipio_residencia=self,
            uci__clave=1,
            resultado__clave=1).count()

    @cached_property
    def criticos_sospechosos(self):
        return (
            Caso.objects
                .filter(
                    municipio_residencia=self,
                    resultado__clave=3)
                .exclude(uci__clave=1)
                .count())
