from django.urls import path, include
from .views import RequisitionLogViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'requisition_log', RequisitionLogViewSet)

urlpatterns = [
    path(r'', include((router.urls, 'core'))),
]
