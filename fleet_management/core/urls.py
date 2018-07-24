from django.urls import path, include
from django.conf.urls import url
# from .views import api_root


urlpatterns = [
    # url(r'^$', api_root),
    path(r'', include('core.fleet.urls')),
    path(r'', include('core.vehicle.urls')),
]
