from uuid import uuid4

from device import Device
from stateclasses import DeviceState

class Hub():
    def __init__(self, name:str, devices:dict={}) -> None:
        self.uuid = uuid4
        self.name = name
        self.devices = {}

    def pairDevice(self, device:Device) -> None:
        # Here we would have to validate that it connected first
        # and then add it to the list
        self.devices[device.uuid] = device

    def getDeviceState(self, device:Device) -> DeviceState:
        # This is a bit strange to have the device and ask
        # for its info from here. Will have to look into usage
        # I image we would have to look up the device by id
        return device.info

    def listDevices(self) -> dict:
        return self.devices

    def removeDevice(self, device:Device) -> None:
        item = self.devices.get(device.uuid)
        if item:
            del self.devices[device.uuid]
