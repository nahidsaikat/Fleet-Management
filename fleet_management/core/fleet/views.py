from django.shortcuts import render
from rest_framework import viewsets

from .models import Fleet
from .serializers import FleetSerializer


class FleetViewSet(viewsets.ModelViewSet):
    serializer_class = FleetSerializer
    queryset = Fleet.objects.all()

