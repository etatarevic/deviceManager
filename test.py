import unittest
from device import Device

from dwelling import Dwelling
from hub import Hub
from main import Driver
from stateclasses import DeviceState, Location

class TestMain(unittest.TestCase):
    def setUp(self):
        self.dwelling = Dwelling("Dwelling Name", Location("123 Main Street", "SLC", "UT", "84121", "US"))
        self.hub = Hub("Hub Name")
        self.device = Device("Device Name")

    def test_remove_dwelling(self):
        self.dwelling.removeDwelling()
        self.assertIsNone(self.dwelling.listDwellings().get(self.dwelling.uuid))

    def test_add_dwelling(self):
        self.dwelling.addDwelling()
        self.assertEqual(self.dwelling.listDwellings()[self.dwelling.uuid], self.dwelling)

    def test_add_hub(self):
        self.dwelling.installHub(self.hub)
        self.assertEqual(self.dwelling.installed_hub, self.hub)

    def test_set_occupied_dwelling(self):
        self.dwelling.setOccupancy(True)
        self.assertEqual(self.dwelling.is_occupied, True)

    def test_pair_device(self):
        self.hub.pairDevice(self.device)
        self.assertEqual(self.hub.listDevices().get(self.device.uuid), self.device)

    def test_remove_device(self):
        self.hub.removeDevice(self.device)
        self.assertIsNone(self.hub.listDevices().get(self.device.uuid))

    def test_device_state(self):
        self.assertEqual(self.hub.getDeviceState(self.device), self.device.info)

    def test_create_device(self):
        self.device.create()
        self.assertEqual(self.device.list().get(self.device.uuid), self.device)

    def test_modify(self):
        newDeviceState = DeviceState(connected=True, waiting=False, happiness=100)
        self.device.modify(newDeviceState)
        self.assertEqual(self.device.info.connected, newDeviceState.connected)
        self.assertEqual(self.device.info.happiness, newDeviceState.happiness)

    def test_full_flow(self):
        Driver.get_devices().clear()
        Driver.get_dwellings().clear()
        dwelling = Dwelling("Flow", Location("123 Main Street", "SLC", "UT", "84121", "US"))
        hub = Hub("Hub Flow")
        device = Device("Device Flow")
        device2 = Device("Device Flow 2")

        dwelling.addDwelling()
        dwelling.installHub(hub)
        device.create()
        device2.create()
        self.assertEqual(len(device.list()), 2)
        self.assertEqual(len(hub.devices), 0)
        hub.pairDevice(device)
        hub.pairDevice(device2)
        self.assertEqual(len(hub.devices), 2)
        hub.removeDevice(device)
        hub.removeDevice(device2)
        self.assertEqual(len(hub.devices), 0)


if __name__ == '__main__':
    unittest.main()