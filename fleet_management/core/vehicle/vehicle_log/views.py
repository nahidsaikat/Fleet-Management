from rest_framework import viewsets

from .models import VehicleLog
from .serializers import VehicleLogSerializer

class VehicleLogViewSet(viewsets.ModelViewSet):
    queryset = VehicleLog.objects.all()
    serializer_class = VehicleLogSerializer
