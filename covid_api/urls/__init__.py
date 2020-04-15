from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from covid_api.urls.routers import router


schema_view = get_schema_view(
   openapi.Info(
      title="COVID-19 Mexico",
      default_version='v1',
      description="API REST para la consulta de casos COVID-19 en México",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="smartinez@conabio.gob.mx"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    url('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
