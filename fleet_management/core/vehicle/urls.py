from django.urls import path, include
from .views import VehicleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet)

urlpatterns = [
    path(r'api/', include((router.urls, 'core'), namespace='vehicle')),
    path(r'api/log/', include('core.vehicle.vehicle_log.urls')),
]
