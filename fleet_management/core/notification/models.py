from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User as SecondUser


class Notification(models.Model):
    message = models.TextField(null=False)
    from_employee_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    to_employee_id = models.ForeignKey(SecondUser, on_delete=models.DO_NOTHING)
    table_name = models.CharField(max_length=255, null=False)
    table_id = models.IntegerField(null=False)
    mark_as_read = models.IntegerField(null=False)
