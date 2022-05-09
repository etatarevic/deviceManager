
class Manager():
    def __init__(self) -> None:
        self.dwellings = {}
        self.devices = {}

class Driver():
    _manager = Manager()

    @staticmethod
    def get_dwellings() -> dict:
        return Driver._manager.dwellings

    @staticmethod
    def get_devices() -> dict:
        return Driver._manager.devices

def main():
    _ = Driver()
    
if __name__=="__main__":
    main()