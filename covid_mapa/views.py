from django.views.generic.base import TemplateView


class MapaVista(TemplateView):
    template_name = "covid_mapa/index.html"
