from django.db import IntegrityError
from django.test import TestCase
from device.models.device import Device
from device.models.deviceState import DeviceState
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

    def test_pair_device(self):
        self.hub.devices.add(self.device)
        self.assertEquals(self.hub.devices.count(), 1)

    def test_pair_same_device_doesnt_change_count(self):
        self.hub.devices.add(self.device)
        self.assertEquals(self.hub.devices.count(), 1)
        self.hub.devices.add(self.device)
        self.assertEquals(self.hub.devices.count(), 1)

    def test_remove_device(self):
        self.hub.devices.remove(self.device)
        self.assertEquals(self.hub.devices.count(), 0)
