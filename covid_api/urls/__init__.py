from django.conf.urls import url
from django.urls import path, include

from covid_api.urls.routers import router
from covid_api.urls.schema import schema_view


urlpatterns = [
    path('', include(router.urls)),
    url('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema'),
    url('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
