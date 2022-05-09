



from uuid import uuid4
from main import Driver

from stateclasses import DeviceState

class Device():
    def __init__(self, name:str, info:DeviceState=DeviceState()) -> None:
        self.uuid = uuid4()
        self.name = name
        self.info = info

    def create(self) -> None:
        Driver.get_devices()[self.uuid] = self

    def delete(self) -> None:
        item = Driver.get_devices().get(self.uuid)
        if item:
            del Driver.get_devices()[self.uuid]

    def getInfo(self) -> DeviceState:
        return self.info

    def modify(self, newState:DeviceState) -> None:
        self.info = newState

    def list(self) -> dict:
        return Driver.get_devices()