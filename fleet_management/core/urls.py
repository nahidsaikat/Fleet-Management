from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path(r'', include('core.fleet.urls')),
    path(r'', include('core.vehicle.urls')),
]
