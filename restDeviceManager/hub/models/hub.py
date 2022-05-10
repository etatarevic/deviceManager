from uuid import uuid4
from django.db import models

from device.models.device import Device

class Hub(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    devices = models.ManyToManyField(Device, related_name='devices', blank=True)
