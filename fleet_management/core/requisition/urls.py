from django.conf.urls import url, include
from .views import RequisitionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'requisition', RequisitionViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='requisition')),
]
