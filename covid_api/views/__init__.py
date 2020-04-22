from covid_api.views.caso import CasoViewSet
from covid_api.views.conteo import ConteoView
from covid_api.views.entidad import EntidadViewSet
from covid_api.views.municipio import MunicipioViewSet
from covid_api.views.catalogos import CatalogoNacionalidadVista
from covid_api.views.catalogos import CatalogoOrigenVista
from covid_api.views.catalogos import CatalogoPaisVista
from covid_api.views.catalogos import CatalogoResultadoVista
from covid_api.views.catalogos import CatalogoSectorVista
from covid_api.views.catalogos import CatalogoSexoVista
from covid_api.views.catalogos import CatalogoSiNoVista
from covid_api.views.catalogos import CatalogoTipoPacienteVista
from covid_api.views.adicionales import MunicipioPoblacionViewSet
from covid_api.views.adicionales import EntidadPoblacionViewSet


__all__ = [
    'CasoViewSet',
    'ConteoView',
    'EntidadViewSet',
    'MunicipioViewSet',
    'CatalogoNacionalidadVista',
    'CatalogoOrigenVista',
    'CatalogoPaisVista',
    'CatalogoResultadoVista',
    'CatalogoSectorVista',
    'CatalogoSexoVista',
    'CatalogoSiNoVista',
    'CatalogoTipoPacienteVista',
    'MunicipioPoblacionViewSet',
    'EntidadPoblacionViewSet',
]
