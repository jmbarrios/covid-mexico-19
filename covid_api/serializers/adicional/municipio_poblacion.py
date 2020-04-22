from rest_framework import serializers
from covid_datos_adicionales.models import MunicipioPoblacion


CAMPOS_EXTRA = [
    "pm0019",
    "ppm0019",
    "pf0019",
    "ppf0019",
    "pt0019",
    "ppt0019",
    "pm2024",
    "ppm2024",
    "pf2024",
    "ppf2024",
    "pt2024",
    "ppt2024",
    "pm2529",
    "ppm2529",
    "pf2529",
    "ppf2529",
    "pt2529",
    "ppt2529",
    "pm3034",
    "ppm3034",
    "pf3034",
    "ppf3034",
    "pt3034",
    "ppt3034",
    "pm3539",
    "ppm3539",
    "pf3539",
    "ppf3539",
    "pt3539",
    "ppt3539",
    "pm4044",
    "ppm4044",
    "pf4044",
    "ppf4044",
    "pt4044",
    "ppt4044",
    "pm4549",
    "ppm4549",
    "pf4549",
    "ppf4549",
    "pt4549",
    "ppt4549",
    "pm5054",
    "ppm5054",
    "pf5054",
    "ppf5054",
    "pt5054",
    "ppt5054",
    "pm5559",
    "ppm5559",
    "pf5559",
    "ppf5559",
    "pt5559",
    "ppt5559",
    "pm6064",
    "ppm6064",
    "pf6064",
    "ppf6064",
    "pt6064",
    "ppt6064",
    "pm65ym",
    "ppm65ym",
    "pf65ym",
    "ppf65ym",
    "pt65ym",
    "ppt65ym",
]


class IdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {'municipio': obj.municipio.clave}
        return self.reverse(
            view_name,
            kwargs=kwargs,
            request=request,
            format=format)


class MunicipioPoblacionListSerializer(serializers.ModelSerializer):
    url = IdentityField(view_name='municipiopoblacion-detail')

    pm = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina total"))
    pf = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina total"))
    pt = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total del municipio"))

    municipio = serializers.SlugRelatedField(
        read_only=True,
        slug_field='clave')
    municipio_clave = serializers.SlugRelatedField(
        read_only=True,
        source='municipio',
        slug_field='clave_municipio')
    municipio_descripcion = serializers.SlugRelatedField(
        read_only=True,
        source='municipio',
        slug_field='descripcion')

    entidad_clave = serializers.SlugRelatedField(
        read_only=True,
        source='municipio.entidad',
        slug_field='clave')
    entidad_descripcion = serializers.SlugRelatedField(
        read_only=True,
        source='municipio.entidad',
        slug_field='descripcion')

    municipio_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='municipio',
        view_name='municipio-detail',
        lookup_field='clave')
    entidad_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source='municipio__entidad',
        view_name='municipio-detail',
        lookup_field='clave')

    class Meta:
        model = MunicipioPoblacion
        fields = [
            'url',
            'municipio',
            'municipio_clave',
            'municipio_descripcion',
            'entidad_clave',
            'entidad_descripcion',
            'municipio_url',
            'entidad_url',
            'pm',
            'pf',
            'pt'
        ]


class MunicipioPoblacionSerializer(MunicipioPoblacionListSerializer):
    ppm = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina total"))
    ppf = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina total"))
    ppt = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de referencia, total"))
    pm0019 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 0 a 19 años"))
    ppm0019 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 0 a 19 años con respecto al total"))
    pf0019 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 0 a 19 años"))
    ppf0019 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 0 a 19 años con respecto al total"))
    pt0019 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 0 a 19 años"))
    ppt0019 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 0 a 19 años con respecto al total"))
    pm2024 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 20 a 24 años"))
    ppm2024 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 20 a 24 años con respecto al total"))
    pf2024 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 20 a 24 años"))
    ppf2024 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 20 a 24 años con respecto al total"))
    pt2024 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 20 a 24 años"))
    ppt2024 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 20 a 24 años con respecto al total"))
    pm2529 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 25 a 29 años"))
    ppm2529 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 25 a 29años con respecto al total"))
    pf2529 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Población femenina de 25 a 29 años"))
    ppf2529 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 25 a 29 años con respecto al total"))
    pt2529 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 25 a 29 años"))
    ppt2529 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 25 a 29 años con respecto al total"))
    pm3034 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 30 a 34 años"))
    ppm3034 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 30 a 34 años con respecto al total"))
    pf3034 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Población femenina de 30 a 34 años"))
    ppf3034 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 30 a 34 años con respecto al total"))
    pt3034 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 30 a 34 años"))
    ppt3034 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 30 a 34 años con respecto al total"))
    pm3539 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 35 a 39 años"))
    ppm3539 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 35 a 39 años con respecto al total"))
    pf3539 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 35 a 39 años"))
    ppf3539 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 35 a 39 años con respecto al total"))
    pt3539 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 35 a 39 años"))
    ppt3539 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 35 a 39 años con respecto al total"))
    pm4044 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 40 a 44 años"))
    ppm4044 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 40 a 44 años con respecto al total"))
    pf4044 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 40 a 44 años"))
    ppf4044 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 40 a 44 años con respecto al total"))
    pt4044 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 40 a 44 años"))
    ppt4044 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 40 a 44 años con respecto al total"))
    pm4549 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 45 a 49 años"))
    ppm4549 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 45 a 49 años con respecto al total"))
    pf4549 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 45 a 49 años"))
    ppf4549 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 45 a 49 años con respecto al total"))
    pt4549 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 45 a 49 años"))
    ppt4549 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 45 a 49 años con respecto al total"))
    pm5054 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 50 a 54 años"))
    ppm5054 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 50 a 54 años con respecto al total"))
    pf5054 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 50 a 54 años"))
    ppf5054 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 50 a 54 años con respecto al total"))
    pt5054 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 50 a 54 años"))
    ppt5054 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 50 a 54 años con respecto al total"))
    pm5559 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 55 a 59 años"))
    ppm5559 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 55 a 59 años con respecto al total"))
    pf5559 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 55 a 59 años"))
    ppf5559 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 55 a 59 años con respecto al total"))
    pt5559 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 55 a 59 años"))
    ppt5559 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 55 a 59 años con respecto al total"))
    pm6064 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 60 a 64 años"))
    ppm6064 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 60 a 64 años con respecto al total"))
    pf6064 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 60 a 64 años"))
    ppf6064 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 60 a 64 años con respecto al total"))
    pt6064 = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 60 a 64 años"))
    ppt6064 = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 60 a 64 años con respecto al total"))
    pm65ym = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población masculina de 65 años y más"))
    ppm65ym = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población masculina de 65 años y más con respecto al total"))
    pf65ym = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población femenina de 65 años y más"))
    ppf65ym = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población femenina de 65 años y más con respecto al total"))
    pt65ym = serializers.IntegerField(
        allow_null=True,
        help_text=(
            "Población total de 65 años y más"))
    ppt65ym = serializers.FloatField(
        allow_null=True,
        help_text=(
            "Porcentaje de la población total de 65 años y más con respecto al total"))

    class Meta:
        model = MunicipioPoblacion
        fields = [
            'url',
            'municipio',
            'municipio_clave',
            'municipio_descripcion',
            'entidad_clave',
            'entidad_descripcion',
            'municipio_url',
            'entidad_url',
            "pm",
            "ppm",
            "pf",
            "ppf",
            "pt",
            "ppt",
            "pm0019",
            "ppm0019",
            "pf0019",
            "ppf0019",
            "pt0019",
            "ppt0019",
            "pm2024",
            "ppm2024",
            "pf2024",
            "ppf2024",
            "pt2024",
            "ppt2024",
            "pm2529",
            "ppm2529",
            "pf2529",
            "ppf2529",
            "pt2529",
            "ppt2529",
            "pm3034",
            "ppm3034",
            "pf3034",
            "ppf3034",
            "pt3034",
            "ppt3034",
            "pm3539",
            "ppm3539",
            "pf3539",
            "ppf3539",
            "pt3539",
            "ppt3539",
            "pm4044",
            "ppm4044",
            "pf4044",
            "ppf4044",
            "pt4044",
            "ppt4044",
            "pm4549",
            "ppm4549",
            "pf4549",
            "ppf4549",
            "pt4549",
            "ppt4549",
            "pm5054",
            "ppm5054",
            "pf5054",
            "ppf5054",
            "pt5054",
            "ppt5054",
            "pm5559",
            "ppm5559",
            "pf5559",
            "ppf5559",
            "pt5559",
            "ppt5559",
            "pm6064",
            "ppm6064",
            "pf6064",
            "ppf6064",
            "pt6064",
            "ppt6064",
            "pm65ym",
            "ppm65ym",
            "pf65ym",
            "ppf65ym",
            "pt65ym",
            "ppt65ym",
        ]
