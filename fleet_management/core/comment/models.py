from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    table_name = models.CharField(max_length=255, null=False)
    table_id = models.IntegerField(null=False)
    comments = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
