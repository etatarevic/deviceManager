from uuid import uuid4
from django.db import models
from .location import Location

from hub.models.hub import Hub

class Dwelling(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    location = models.OneToOneField(Location, related_name='location', on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)
    installed_hub = models.OneToOneField(Hub, related_name='hub', on_delete=models.CASCADE, null=True)

