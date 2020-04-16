from rest_framework.generics import ListAPIView
from covid_data.models import Caso


class ConteoView(ListAPIView):
    def get_queryset(self):
        pass
