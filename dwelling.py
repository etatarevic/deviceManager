from hub import Hub
from main import Driver
from stateclasses import Location
from uuid import uuid4

class Dwelling():

    def __init__(self, name:str, location:Location) -> None:
        self.name = name
        self.location = location
        self.uuid = uuid4
        self.is_occupied = False
        self.installed_hub = None
    
    def installHub(self, hub:Hub) -> None:
        self.installed_hub = hub

    def listDwellings(self) -> dict:
        return Driver.get_dwellings()

    def setOccupancy(self, is_occupied:bool) -> None:
        self.is_occupied = is_occupied

    def addDwelling(self) -> None:
        Driver.get_dwellings()[self.uuid] = self

    def removeDwelling(self) -> None:
        item = Driver.get_dwellings().get(self.uuid)
        if item:
            del Driver.get_dwellings()[self.uuid]
