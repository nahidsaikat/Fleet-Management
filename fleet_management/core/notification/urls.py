from django.conf.urls import url, include
from .views import NotificationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='notification')),
]
