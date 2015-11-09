from battleship.interface.tty import TTY
from battleship.utils.utils import Utils

__author__ = 'jitrixis'


class Boat:
    def __init__(self):
        self._length = None
        self._location = None

    def get_length(self):
        return self._length

    def get_location(self):
        return self._location

    def set_location(self, location):
        Utils.check_location(location)
        self._location = location
        return self

    def visual_set_location(self):
        self.set_location(TTY.boat_set_location())

    def is_ready(self):
        return self._location is not None

    def in_location(self, location):
        if not self._location[2]:
            if self._location[0] <= location[0] < self._location[0]+self._length:
                return True
        else:
            if self._location[1] <= location[1] < self._location[1]+self._length:
                return True
        return False


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
