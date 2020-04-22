from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoPaisVista(CatalogoVista):
    queryset = models.Pais.objects.all()
    serializer_class = otros.PaisSerializer

    def list(self, *args, **kwargs):
        """
        Pais - Valores posibles.

        Regresa la lista de paises del mundo asociados a la información por
        clave. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/paises/

        """
        return super().list(*args, **kwargs)
