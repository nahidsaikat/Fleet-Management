from rest_framework import viewsets

from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        serializer.save()
