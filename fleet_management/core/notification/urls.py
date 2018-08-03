from django.urls import path, include
from .views import NotificationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    path(r'api/', include((router.urls, 'core'), namespace='notification')),
]
