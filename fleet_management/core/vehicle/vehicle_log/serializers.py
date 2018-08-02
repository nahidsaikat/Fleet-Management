from rest_framework import serializers
from .models import VehicleLog


class VehicleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLog
        fields = ('id', 'requisition', 'from_status', 'to_status', 'date_time', 'user')
