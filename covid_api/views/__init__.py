from covid_api.views.caso import CasoViewSet
from covid_api.views.entidad import EntidadViewSet
from covid_api.views.municipio import MunicipioViewSet
from covid_api.views.nacionalidad import NacionalidadViewSet
from covid_api.views.origen import OrigenViewSet
from covid_api.views.pais import PaisViewSet
from covid_api.views.resultado import ResultadoViewSet
from covid_api.views.sector import SectorViewSet
from covid_api.views.sexo import SexoViewSet
from covid_api.views.si_no import SiNoViewSet
from covid_api.views.tipo_paciente import TipoPacienteViewSet


__all__ = [
    'CasoViewSet',
    'EntidadViewSet',
    'MunicipioViewSet',
    'NacionalidadViewSet',
    'OrigenViewSet',
    'PaisViewSet',
    'ResultadoViewSet',
    'SectorViewSet',
    'SexoViewSet',
    'SiNoViewSet',
    'TipoPacienteViewSet',
]
