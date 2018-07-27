from django.conf.urls import url, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comment', CommentViewSet)

urlpatterns = [
    url(r'^', include((router.urls, 'core'), namespace='comment')),
]
