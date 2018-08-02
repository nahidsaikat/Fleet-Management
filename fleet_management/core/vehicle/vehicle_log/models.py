from django.db import models
from django.contrib.auth.models import User

from core.vehicle.models import Vehicle


class VehicleLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    from_status = models.CharField(max_length=30)
    to_status = models.CharField(max_length=30, null=False)
    remarks = models.CharField()
