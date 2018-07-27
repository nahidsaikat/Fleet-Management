from django.conf.urls import url, include
from .views import VehicleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='vehicle')),
]
