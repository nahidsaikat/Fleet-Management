from django.conf.urls import url, include
from .views import FleetViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'fleet', FleetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
