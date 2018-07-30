from rest_framework import viewsets

from .models import Requisition
from .serializers import RequisitionSerializer

class RequisitionViewSet(viewsets.ModelViewSet):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

    def perform_create(self, serializer):
        serializer.save()
