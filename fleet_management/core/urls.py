from django.urls import path, include

urlpatterns = [
    path(r'', include('core.fleet.urls')),
    path(r'', include('core.vehicle.urls')),
    path(r'', include('core.vehicle.vehicle_log.urls')),
    path(r'', include('core.requisition.urls')),
    path(r'', include('core.requisition.requisition_log.urls')),
    path(r'', include('core.comment.urls')),
    path(r'', include('core.notification.urls')),
]
