from django.urls import path, include


urlpatterns = [
    path(r'', include('core.fleet.urls')),
    path(r'', include('core.vehicle.urls')),
]
