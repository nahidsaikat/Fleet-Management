from django.urls import path, include
from .views import FleetViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'fleet', FleetViewSet)

urlpatterns = [
    path(r'api/', include((router.urls, 'core'), namespace='fleet')),
]
