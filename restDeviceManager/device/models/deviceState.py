from django.db import models

class DeviceState(models.Model):
    connected = models.BooleanField(default=False)
    waiting = models.BooleanField(default=False)
    happiness = models.IntegerField(default=0)