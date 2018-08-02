from django.db import models
from django.contrib.auth.models import User

from core.requisition.models import Requisition


class VehicleLog(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    from_status = models.CharField(max_length=30)
    to_status = models.CharField(max_length=30)
    date_time = models.DateTimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
