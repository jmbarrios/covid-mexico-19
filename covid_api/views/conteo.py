from django.db.models import Count
from rest_framework.response import Response
from covid_data.models import Caso
from covid_api import filters
from covid_api.serializers.conteo import CasoConteoSerializer
from covid_api.views.base import ListViewSet
from covid_api.views.caso import campos_relacionales
from covid_api.views.caso import campos
from covid_api.views.caso import campos_clave


only = (
    campos +
    [f'{campo}__clave' for campo in campos_clave] +
    [f'{campo}__descripcion' for campo in campos_relacionales + campos_clave]
)


class ConteoView(ListViewSet):
    """
    Conteo de casos agrupados por las columnas deseadas.

    Es posible aplicar filtros sobre la lista de casos y así obtener
    el conteo sobre los casos que lo satisfacen. Por ejemplo, si se
    desea obtener el número de casos positivos por municipio:

        <host:port>/api/conteos?columna=municipio_residencia&positivo=si

    La vista permite seleccionar varias columnas simultáneamente. Si
    se desea obtener el número de defunciones por entidad, sexo y edad:

        <host:port>/api/conteos?columna=entidad_residencia&columna=sexo&columna=edad&defuncion=si

    """

    queryset = (
        Caso.objects
        .all()
        .prefetch_related(*campos_relacionales)
        .only(*only))
    filterset_class = filters.CasoConteoFilter
    serializer_class = CasoConteoSerializer

    def list(self, request, *args, **kwargs):
        """
        Conteo de casos agrupados por columnas.

        Es posible aplicar filtros sobre la lista de casos y así obtener
        el conteo sobre los casos que lo satisfacen. Por ejemplo, si se
        desea obtener el número de casos positivos por municipio:

            <host:port>/api/conteos?columna=municipio_residencia&positivo=si

        La vista permite seleccionar varias columnas simultáneamente. Si
        se desea obtener el número de defunciones por entidad, sexo y edad:

            <host:port>/api/conteos?columna=entidad_residencia&columna=sexo&columna=edad&defuncion=si

        Las columnas por las cuales se pueden agrupar los casos son:

        |  |  |  |
        | --- | --- | --- |
        | 1. fecha_actualizacion | 13. tipo_paciente | 25. cardiovascular |
        | 2. fecha_ingreso | 14. intubado | 26. obesidad |
        | 3. fecha_sintomas | 15. neumonia | 27. renal_cronica |
        | 4. fecha_defuncion | 16. nacionalidad | 28. tabaquismo |
        | 5. edad | 17. embarazo | 29. otro_caso |
        | 6. origen | 18. habla_lengua_indigena | 30. resultado |
        | 7. sector | 19. diabetes | 31. migrante |
        | 8. entidad_um | 20. epoc | 32. pais_nacionalidad |
        | 9. sexo | 21. asma | 33. pais_origen |
        | 10. entidad_nacimiento | 22. inmusupr | 34. uci |
        | 11. entidad_residencia | 23. hipertension | |
        | 12. municipio_residencia | 24. otras_com | |

        Las respuestas en formato JSON están estructuradas de la siguiente manera:

            [
                {
                    "conteo": número de casos en este grupo de después del filtrado,
                    "<columna de agrupacion 1>": <valor en columna 1 de este grupo>,
                    "<columna de agrupacion 2>": <valor en columna 2 de este grupo>,
                    ...
                },
                ...
            ]
        """
        columnas = self.request.GET.getlist('columna')
        queryset = self.filter_queryset(self.get_queryset())

        if not columnas:
            queryset = queryset.aggregate(conteo=Count('renglon'))
            serializer = self.get_serializer(
                queryset, many=False, columnas=columnas)
            return Response(serializer.data)

        queryset = queryset.annotate(conteo=Count('renglon'))

        if 'ordenar' in self.request.GET:
            ordenar = self.request.GET['ordenar']

            opciones = []
            for col in columnas + ['conteo']:
                opciones += [col, f'-{col}']

            if ordenar in opciones:
                queryset = queryset.order_by(ordenar)
            else:
                queryset = queryset.order_by('-conteo')
        else:
            queryset = queryset.order_by('-conteo')

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(
                page, many=True, columnas=columnas)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            queryset, many=True, columnas=columnas)
        return Response(serializer.data)
