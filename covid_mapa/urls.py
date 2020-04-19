from django.urls import path

from covid_mapa.views import MapaVista

urlpatterns = [
    path('', MapaVista.as_view(), name='mapa'),
]
