from covid_graphql.types import GeometryScalar
from graphene_django.converter import convert_django_field
from django.contrib.gis.db.models import MultiPolygonField, PointField

@convert_django_field.register(MultiPolygonField)
@convert_django_field.register(PointField)
def convert_geom_to_jsonField(field, registry=None):
    return GeometryScalar()