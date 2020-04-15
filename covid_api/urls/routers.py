from rest_framework import routers
from covid_api import views


router = routers.DefaultRouter()
router.register('entidad', views.EntidadViewSet, basename='entidad')
router.register('sexo', views.SexoViewSet)
router.register('origen', views.OrigenViewSet)
router.register('sector', views.SectorViewSet)
router.register('nacionalidad', views.NacionalidadViewSet)
router.register('tipo_paciente', views.TipoPacienteViewSet)
router.register('resultado', views.ResultadoViewSet)
router.register('pais', views.PaisViewSet)
router.register('municipio', views.MunicipioViewSet)
router.register('si_no', views.SiNoViewSet)
router.register('caso', views.CasoViewSet)
