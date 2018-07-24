from rest_framework import viewsets

from .models import Fleet
from .serializers import FleetSerializer

class FleetViewSet(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer

    def perform_create(self, serializer):
        serializer.save()
