from rest_framework import routers
from covid_api import views

router = routers.DefaultRouter()
router.register(r'sexo', views.SexoViewSet)
router.register(r'origen', views.OrigenViewSet)
router.register(r'sector', views.SectorViewSet)
router.register(r'entidad', views.EntidadViewSet)
router.register(r'nacionalidad', views.NacionalidadViewSet)
router.register(r'tipo_paciente', views.TipoPacienteViewSet)
router.register(r'resultado', views.ResultadoViewSet)
router.register(r'pais', views.PaisViewSet)
router.register(r'municipio', views.MunicipioViewSet)
router.register(r'si_no', views.SiNoViewSet)
router.register(r'caso', views.CasoViewSet)
router.register(r'entidad_geo', views.EntidadGeoViewSet)
router.register(r'municipio_geo', views.MunicipioGeoViewSet)
