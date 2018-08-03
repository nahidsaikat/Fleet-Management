from django.urls import path, include
from .views import RequisitionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'requisition', RequisitionViewSet)

urlpatterns = [
    path(r'api/', include((router.urls, 'core'), namespace='requisition')),
    path(r'api/log/', include(('core.requisition.requisition_log.urls', 'core'), namespace='requisition_log')),
]
