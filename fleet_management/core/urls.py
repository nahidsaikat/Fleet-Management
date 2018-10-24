from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path(r'', dashboard, name='home'),
    path(r'', include('core.fleet.urls')),
    path(r'', include('core.vehicle.urls')),
    path(r'', include('core.requisition.urls')),
    path(r'', include('core.comment.urls')),
    path(r'', include('core.notification.urls')),
]
