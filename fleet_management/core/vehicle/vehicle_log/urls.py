from django.urls import path, include
from .views import VehicleLogViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'vehicle_log', VehicleLogViewSet)

urlpatterns = [
    path(r'', include((router.urls, 'core'), namespace='vehicle_log')),
]
