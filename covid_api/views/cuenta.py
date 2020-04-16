from rest_framework.generics import ListAPIView
from covid_data.models import Caso


class ConteoView(ListAPIView):
    queryset = Caso.objects.all()

    def get_queryset(self):
        pass
