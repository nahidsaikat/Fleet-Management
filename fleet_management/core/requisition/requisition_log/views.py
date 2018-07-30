from rest_framework import viewsets

from .models import RequisitionLog
from .serializers import RequisitionLogSerializer

class RequisitionLogViewSet(viewsets.ModelViewSet):
    queryset = RequisitionLog.objects.all()
    serializer_class = RequisitionLogSerializer
