from django.db import models
from django.contrib.auth.models import User

from core.vehicle.models import Vehicle


class Requisition(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    from_date = models.DateField(null=False)
    from_time = models.TimeField(null=False)
    to_date = models.DateField(null=False)
    to_time = models.TimeField(null=False)
    status = models.CharField(max_length=30, null=False)
    requisition_by = models.ForeignKey(User, on_delete=models.CASCADE)
