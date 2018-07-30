from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User as SecondUser


class Notification(models.Model):
    message = models.TextField(null=False)
    from_employee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_from_employee')
    to_employee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_to_employee')
    table_name = models.CharField(max_length=255, null=False)
    table_id = models.IntegerField(null=False)
    mark_as_read = models.IntegerField(null=False)
