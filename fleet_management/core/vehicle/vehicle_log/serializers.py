from rest_framework import serializers
from .models import VehicleLog


class VehicleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLog
        fields = ('id', 'vehicle', 'driver', 'from_status', 'to_status', 'remarks')
