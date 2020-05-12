from graphene import (Connection, 
                      ConnectionField, 
                      Int, 
                      List, 
                      Node, 
                      ObjectType,
                      Schema)

from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from covid_data.models import Caso, Sector, Entidad
from covid_api.filters.caso import CasoFilter

from covid_graphql.converter import convert_geom_to_jsonField


class SectorType(DjangoObjectType):
    class Meta:
        model = Sector


class CasoNodeType(DjangoObjectType):
    class Meta:
        model = Caso
        interfaces = (Node, )
        filterset_class = CasoFilter


class EntidadType(DjangoObjectType):
    class Meta:
        model = Entidad
        fields = ('clave', 'descripcion', 'centroide')

# class CasoConnectionType(Connection):
#     class Meta:
#         node = CasoNodeType


class QueryType(ObjectType):
    all_sectors = List(SectorType)
    # get_casos = List(CasoType)
    # get_casos = ConnectionField(CasoConnectionType)
    get_casos = DjangoFilterConnectionField(CasoNodeType)

    def resolve_all_sectors(self, info, **kwargs):
        return Sector.objects.all()

    # def resolve_get_casos(self, info, **kwargs):
    #     return Caso.objects.all()

schema = Schema(query=QueryType)
