from battleship.utils.utils import Utils

__author__ = 'jitrixis'


class Boat:
    def __init__(self):
        self._length = None
        self._location = None
        self.__ready = False

    def getLocation(self):
        return self._location

    def setLocation(self, location):
        Utils.check_location(location)
        self._location = location
        self.__ready = True
        return self

    def isReady(self):
        return self.__ready


class BoatAircraftCarrier(Boat):
    def __init__(self):
        super().__init__()
        self._length = 5


class BoatBattleShip(Boat):
    def __init__(self):
        super().__init__()
        self._length = 4


class BoatCruiser(Boat):
    def __init__(self):
        super().__init__()
        self._length = 3


class BoatDestroyer(Boat):
    def __init__(self):
        super().__init__()
        self._length = 2


class BoatSubmarine(Boat):
    def __init__(self):
        super().__init__()
        self._length = 1
