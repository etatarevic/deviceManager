from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    sate = models.CharField(max_length=64, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=10, blank=True)
