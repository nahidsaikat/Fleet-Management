from rest_framework import serializers
from .models import RequisitionLog


class RequisitionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionLog
        fields = ('id', 'requisition', 'from_status', 'to_status', 'date_time', 'user')
