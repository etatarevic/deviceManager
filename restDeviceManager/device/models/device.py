from uuid import uuid4
from django.db import models

from .deviceState import DeviceState

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    info = models.OneToOneField(DeviceState, related_name='info', on_delete=models.CASCADE)
