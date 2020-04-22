from rest_framework import routers

from covid_api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register('entidades', views.EntidadViewSet)
router.register('municipios', views.MunicipioViewSet)
router.register('casos', views.CasoViewSet)
router.register('conteos', views.ConteoView, basename='conteo')

router.register(
    'catalogos/nacionalidad',
    views.CatalogoNacionalidadVista,
    basename='catalogo-nacionalidad')
router.register(
    'catalogos/origen',
    views.CatalogoOrigenVista,
    basename='catalogo-origen')
router.register(
    'catalogos/paises',
    views.CatalogoPaisVista,
    basename='catalogo-pais')
router.register(
    'catalogos/resultado',
    views.CatalogoResultadoVista,
    basename='catalogo-resultado')
router.register(
    'catalogos/sector',
    views.CatalogoSectorVista,
    basename='catalogo-sector')
router.register(
    'catalogos/sexo',
    views.CatalogoSexoVista,
    basename='catalogo-sexo')
router.register(
    'catalogos/si_no',
    views.CatalogoSiNoVista,
    basename='catalogo-sino')
router.register(
    'catalogos/tipo_paciente',
    views.CatalogoTipoPacienteVista,
    basename='catalogo-tipopaciente')

router.register(
    'poblacion/municipios',
    views.MunicipioPoblacionViewSet,
    basename='municipiopoblacion')
router.register(
    'poblacion/entidades',
    views.EntidadPoblacionViewSet,
    basename='entidadpoblacion')
