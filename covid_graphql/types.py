import json
from graphene.types.scalars import Scalar

class GeometryScalar(Scalar):

    @staticmethod
    def serialize(geom):
        return json.dumps(geom.geojson)

    @staticmethod
    def parse_value(value):
        pass

    @staticmethod
    def parse_literal(node):
        pass