from django.conf.urls import url, include
from .views import VehicleLogViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'log', VehicleLogViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='vehicle_log')),
]
