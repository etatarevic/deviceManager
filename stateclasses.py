from dataclasses import dataclass
from enum import Enum

class DeviceType(Enum):
    Switch = 1
    Dimmer = 2
    Lock = 3
    Thermostat = 4

@dataclass
class Location:
    street_address:str = "123 Main Street"
    city:str = "Salt Lake City"
    state:str = "UT"
    zipcode:str = "84103"
    country:str = "US"

@dataclass
class DeviceState:
    connected:bool = False
    waiting:bool = False
    happiness:int = 0
    type:DeviceType = DeviceType.Switch
