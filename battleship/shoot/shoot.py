from battleship.utils.utils import Utils

__author__ = 'jitrixis'


class Shoot:
    def __init__(self):
        self._location = None
        self._status = None

    def get_location(self):
        return self._location

    def set_location(self, location):
        Utils.check_location(location)
        self._location = location
        return self

    def visual_set_location(self):
        print("ASK SHOOT LOCATION")
        self.set_location(Utils.to_location(0, 0, 0))

    def get_status(self):
        return self._status

    def __iadd__(self, other):
        if type(other) not in []:
            raise TypeError("Type of the second member is not allowed")
        if self.get_location() is None:
            raise ValueError("Shoot has no location")
        other.set_location(self.get_location())
        return other


class ShootFailed(Shoot):
    def __init__(self):
        super().__init__()
        self._status = False

    def set_location(self, location):
        if self._location is not None:
            raise Exception("Shoot cannot be overwritten")

    def __iadd__(self, other):
        raise Exception("Shoot cannot be overwritten")


class ShootSuccessful(Shoot):
    def __init__(self):
        super().__init__()
        self._status = True

    def set_location(self, location):
        if self._location is not None:
            raise Exception("Shoot cannot be overwritten")

    def __iadd__(self, other):
        raise Exception("Shoot cannot be overwritten")
