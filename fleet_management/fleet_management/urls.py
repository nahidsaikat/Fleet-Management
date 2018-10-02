"""fleet_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from authentication import views as auth_views

urlpatterns = [
    # email sign up
    path('account_activation_sent/', auth_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.activate, name='activate'),


    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('', TemplateView.as_view(template_name='layout.html'), name='home'),
]
