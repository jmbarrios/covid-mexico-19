from django.contrib.gis.geos import GEOSGeometry
from graphql.language import ast
from graphene.types.scalars import Scalar

class GISScalar(Scalar):
    @property
    def geom_typeid(self):
        raise NotImplementedError(
            "GEOSScalar is an abstract class and doesn't have a 'geom_typeid'. \
            Instantiate a concrete subtype instead."
        )

    @staticmethod
    def serialize(geometry):
        return eval(geometry.geojson)

    @classmethod
    def parse_literal(cls, node):
        assert isinstance(node, ast.StringValue)
        geometry = GEOSGeometry(node.value)
        return eval(geometry.geojson)

    @classmethod
    def parse_value(cls, node):
        geometry = GEOSGeometry(node.value)
        return eval(geometry.geojson)


class PointScalar(GISScalar):
    class Meta:
        description = "A GIS GeoJSON point"


class MultiPolygonScalar(GISScalar):
    class Meta:
        description = "A GIS MultiPolygon geojson"