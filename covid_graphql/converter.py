from django.contrib.gis.db.models import MultiPolygonField, PointField
from graphene_django.converter import convert_django_field

from covid_graphql.types import MultiPolygonScalar, PointScalar

GIS_FIELD_SCALAR = {
    "PointField": PointScalar,
    "MultiPolygonField": MultiPolygonScalar
}

@convert_django_field.register(MultiPolygonField)
@convert_django_field.register(PointField)
def convert_geom_to_jsonField(field, registry=None):
    class_name = field.__class__.__name__
    return GIS_FIELD_SCALAR[class_name](
        required=not field.null, description=field.help_text
    )
