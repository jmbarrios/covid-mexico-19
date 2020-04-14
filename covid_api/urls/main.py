from django.conf.urls import url, include
from .routers import router


urlpatterns = [
    url(r'^', include(router.urls)),
]
