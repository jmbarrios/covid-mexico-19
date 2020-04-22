from covid_data import models
from covid_api.serializers import otros
from covid_api.views.base import CatalogoVista


class CatalogoTipoPacienteVista(CatalogoVista):
    queryset = models.TipoPaciente.objects.all()
    serializer_class = otros.TipoPacienteSerializer

    def list(self, *args, **kwargs):
        """
        Tipo Paciente - Valores posibles.

        Regresa la lista de valores posibles para *tipo_paciente*, según el
        formato de la información liberada. No requiere parámetros. Ejemplo:

            <host:port>/api/catalogos/tipo_paciente/

        """
        return super().list(*args, **kwargs)
