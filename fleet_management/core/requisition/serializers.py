from rest_framework import serializers
from .models import Requisition


class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = ('id', 'serial', 'fleet', 'status', 'driver')
