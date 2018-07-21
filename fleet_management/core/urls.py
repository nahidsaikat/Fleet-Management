from django.urls import path, include


urlpatterns = [
    path(r'', include('core.fleet.urls')),
]
