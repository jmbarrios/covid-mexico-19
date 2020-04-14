from django.conf.urls import url, include


urlpatterns = [
    url('^', include(('covid_api.urls.main', 'covid_api'))),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
