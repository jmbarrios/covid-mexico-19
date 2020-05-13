from graphene import (Connection, ConnectionField, Int, List, Node, ObjectType,
                      Schema)
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from covid_api.filters.caso import CasoFilter
from covid_data.models import Caso, Entidad, Origen, Sector
from covid_graphql.converter import convert_geom_to_jsonField


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector


class OrigenType(DjangoObjectType):
    class Meta:
        model = Origen


class CasoNodeType(DjangoObjectType):
    class Meta:
        model = Caso
        interfaces = (Node, )
        filterset_class = CasoFilter


class EntidadType(DjangoObjectType):
    class Meta:
        model = Entidad
        fields = ('clave', 
            'descripcion', 
            'centroide', 
            'geometria_simplificada')


class QueryType(ObjectType):
    get_casos = DjangoFilterConnectionField(CasoNodeType)


schema = Schema(query=QueryType)
