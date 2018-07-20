from django.urls import path
from .views import FleetViewSet

app_name = 'core'

urlpatterns = [
    path('fleet/', FleetViewSet.as_view({'get': 'list'}), name='fleet')
]

# from django.conf.urls import include, url
# from .views import FleetViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'fleet', FleetViewSet)
# urlpatterns = router.urls
