from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'from_employee_id', 'to_employee_id', 'table_name', 'table_id', 'mark_as_read')
