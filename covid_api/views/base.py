import datetime
from rest_framework import viewsets
from rest_framework import mixins


class ResponseMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if kwargs.get('format', None) == 'csv':
            vista = self.get_view_name().lower()
            fecha = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
            nombre = f'{vista}_{fecha}.csv'
            response['Content-Disposition'] = f'attachment; filename="{nombre}"'
        return super().finalize_response(request, response, *args, **kwargs)


class ListViewSet(
        ResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    pass


class ListRetrieveViewSet(
        ResponseMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    pass


class CatalogoVista(
        ResponseMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    page_size = None
    pagination_class = None
