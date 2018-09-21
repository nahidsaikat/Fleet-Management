from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup', views.signup, name='signup')
]
