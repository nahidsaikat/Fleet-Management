from django.conf.urls import url, include
from .views import RequisitionLogViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'requisition_log', RequisitionLogViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='requisition_log')),
]
