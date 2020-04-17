from covid_api.views.caso import CasoViewSet
from covid_api.views.entidad import EntidadViewSet
from covid_api.views.municipio import MunicipioViewSet
from covid_api.views.catalogos import CatalogoEntidadesVista
from covid_api.views.catalogos import CatalogoMunicipiosVista
from covid_api.views.catalogos import CatalogoNacionalidadVista
from covid_api.views.catalogos import CatalogoOrigenVista
from covid_api.views.catalogos import CatalogoPaisVista
from covid_api.views.catalogos import CatalogoResultadoVista
from covid_api.views.catalogos import CatalogoSectorVista
from covid_api.views.catalogos import CatalogoSexoVista
from covid_api.views.catalogos import CatalogoSiNoVista
from covid_api.views.catalogos import CatalogoTipoPacienteVista


__all__ = [
    'CasoViewSet',
    'EntidadViewSet',
    'MunicipioViewSet',
    'CatalogoEntidadesVista',
    'CatalogoMunicipiosVista',
    'CatalogoNacionalidadVista',
    'CatalogoOrigenVista',
    'CatalogoPaisVista',
    'CatalogoResultadoVista',
    'CatalogoSectorVista',
    'CatalogoSexoVista',
    'CatalogoSiNoVista',
    'CatalogoTipoPacienteVista',
]
