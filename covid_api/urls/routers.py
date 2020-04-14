from rest_framework import routers
from covid_api import views


router = routers.DefaultRouter()
router.register(r'casos', views.CasosViewSet)
router.register(r'tipo_paciente', views.TipoPacientesViewSet)
