from django.db import IntegrityError
from django.test import TestCase
from .models.device import Device
from .models.deviceState import DeviceState
from hub.models.hub import Hub
from dwelling.models.location import Location
from dwelling.models.dwelling import Dwelling

class TestAPI(TestCase):
    def setUp(self):
        self.location = Location.objects.create(street="123 ABC Street")
        self.hub = Hub.objects.create(name="Hub")
        self.dwelling = Dwelling.objects.create(
            name="d1", 
            location=self.location, 
            is_occupied=True, 
            installed_hub=self.hub
        )
        self.device_info = DeviceState.objects.create()
        self.device = Device.objects.create(name="device", info=self.device_info)

    def test_create_device_with_same_device_info(self):
        with self.assertRaises(IntegrityError):
            Device.objects.create(name="device", info=self.device_info)