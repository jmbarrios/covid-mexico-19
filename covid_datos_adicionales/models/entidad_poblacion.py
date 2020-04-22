from django.db import models
from covid_data.models import Entidad


COLUMNAS_POBLACION = [
    "pm",
    "pf",
    "pt",
    "pm0019",
    "pf0019",
    "pt0019",
    "pm2024",
    "pf2024",
    "pt2024",
    "pm2529",
    "pf2529",
    "pt2529",
    "pm3034",
    "pf3034",
    "pt3034",
    "pm3539",
    "pf3539",
    "pt3539",
    "pm4044",
    "pf4044",
    "pt4044",
    "pm4549",
    "pf4549",
    "pt4549",
    "pm5054",
    "pf5054",
    "pt5054",
    "pm5559",
    "pf5559",
    "pt5559",
    "pm6064",
    "pf6064",
    "pt6064",
    "pm65ym",
    "pf65ym",
    "pt65ym",
]

COLUMNAS_PORCENTAJE = [
    "ppm",
    "ppf",
    "ppt",
    "ppm0019",
    "ppf0019",
    "ppt0019",
    "ppm2024",
    "ppf2024",
    "ppt2024",
    "ppm2529",
    "ppf2529",
    "ppt2529",
    "ppm3034",
    "ppf3034",
    "ppt3034",
    "ppm3539",
    "ppf3539",
    "ppt3539",
    "ppm4044",
    "ppf4044",
    "ppt4044",
    "ppm4549",
    "ppf4549",
    "ppt4549",
    "ppm5054",
    "ppf5054",
    "ppt5054",
    "ppm5559",
    "ppf5559",
    "ppt5559",
    "ppm6064",
    "ppf6064",
    "ppt6064",
    "ppm65ym",
    "ppf65ym",
    "ppt65ym",
]


class EntidadPoblacion(models.Model):
    entidad = models.OneToOneField(
        Entidad,
        on_delete=models.CASCADE)

    pm = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina total"))
    ppm = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina total"))
    pf = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina total"))
    ppf = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina total"))
    pt = models.IntegerField(
        null=True,
        help_text=(
            "Población total del municipio"))
    ppt = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de referencia, total"))
    pm0019 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 0 a 19 años"))
    ppm0019 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total"))
    pf0019 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 0 a 19 años"))
    ppf0019 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total"))
    pt0019 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 0 a 19 años"))
    ppt0019 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total"))
    pm2024 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 20 a 24 años"))
    ppm2024 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total"))
    pf2024 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 20 a 24 años"))
    ppf2024 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total"))
    pt2024 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 20 a 24 años"))
    ppt2024 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total"))
    pm2529 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 25 a 29 años"))
    ppm2529 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total"))
    pf2529 = models.FloatField(
        null=True,
        help_text=(
            "Población femenina de 25 a 29 años"))
    ppf2529 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total"))
    pt2529 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 25 a 29 años"))
    ppt2529 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total"))
    pm3034 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 30 a 34 años"))
    ppm3034 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total"))
    pf3034 = models.FloatField(
        null=True,
        help_text=(
            "Población femenina de 30 a 34 años"))
    ppf3034 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total"))
    pt3034 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 30 a 34 años"))
    ppt3034 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total"))
    pm3539 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 35 a 39 años"))
    ppm3539 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total"))
    pf3539 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 35 a 39 años"))
    ppf3539 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total"))
    pt3539 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 35 a 39 años"))
    ppt3539 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total"))
    pm4044 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 40 a 44 años"))
    ppm4044 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total"))
    pf4044 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 40 a 44 años"))
    ppf4044 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total"))
    pt4044 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 40 a 44 años"))
    ppt4044 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total"))
    pm4549 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 45 a 49 años"))
    ppm4549 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total"))
    pf4549 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 45 a 49 años"))
    ppf4549 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total"))
    pt4549 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 45 a 49 años"))
    ppt4549 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total"))
    pm5054 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 50 a 54 años"))
    ppm5054 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total"))
    pf5054 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 50 a 54 años"))
    ppf5054 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total"))
    pt5054 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 50 a 54 años"))
    ppt5054 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total"))
    pm5559 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 55 a 59 años"))
    ppm5559 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total"))
    pf5559 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 55 a 59 años"))
    ppf5559 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total"))
    pt5559 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 55 a 59 años"))
    ppt5559 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total"))
    pm6064 = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 60 a 64 años"))
    ppm6064 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total"))
    pf6064 = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 60 a 64 años"))
    ppf6064 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total"))
    pt6064 = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 60 a 64 años"))
    ppt6064 = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total"))
    pm65ym = models.IntegerField(
        null=True,
        help_text=(
            "Población masculina de 65 años y más"))
    ppm65ym = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total"))
    pf65ym = models.IntegerField(
        null=True,
        help_text=(
            "Población femenina de 65 años y más"))
    ppf65ym = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total"))
    pt65ym = models.IntegerField(
        null=True,
        help_text=(
            "Población total de 65 años y más"))
    ppt65ym = models.FloatField(
        null=True,
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total"))
