from django.db import models
from django.contrib.auth.models import User

from core.fleet.models import Fleet


class Requisition(models.Model):
    serial = models.CharField(max_length=255, null=False)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, null=False)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
