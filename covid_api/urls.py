from rest_framework import routers
from covid_api.viewsets import CasosViewSet, TipoPacientesViewSet
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'casos', CasosViewSet)
router.register(r'tipo_paciente', TipoPacientesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
