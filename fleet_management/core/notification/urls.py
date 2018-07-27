from django.conf.urls import url, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notification', CommentViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='notification')),
]
