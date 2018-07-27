from rest_framework import serializers
from .models import Requisition


class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = ('id', 'vehicle', 'from_date', 'from_time', 'to_date', 'to_time', 'status', 'requisition_by')
