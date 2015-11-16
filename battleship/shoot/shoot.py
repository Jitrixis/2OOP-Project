from battleship.location.location import Location

__author__ = 'jitrixis'


class Shoot:
    def __init__(self):
        self._location = Location()
        self._status = None

    #GETTERS/SETTERS

    def get_location(self):
        return self._location

    def set_location(self, pos):
        self._location.set_location(pos)
        return self

    def get_status(self):
        return self._status

    #VIEW

    def view_set_location(self):
        self._location.view_init_location()

    #OPERATORS OVERLOADERS

    def __bool__(self):
        return bool(self._location)

    def __contains__(self, other):
        if not self or not other:
            return False
        return self.get_location() in other.get_location()

    def __iadd__(self, other):
        if type(other) not in [ShootFailed, ShootSuccessful]:
            raise TypeError("Type of the second member is not allowed")
        if not self:
            raise ValueError("Shoot has no location")
        other.set_location(self.get_location().get_pos())
        return other


class ShootFailed(Shoot):
    def __init__(self):
        super().__init__()
        self._status = False

    #GETTERS/SETTERS

    def set_location(self, pos):
        if self._location:
            raise Exception("Shoot cannot be overwritten")
        self._location.set_location(pos)

    #OPERATORS OVERLOADERS

    def __iadd__(self, other):
        raise Exception("Shoot cannot be overwritten")


class ShootSuccessful(Shoot):
    def __init__(self):
        super().__init__()
        self._status = True

    #GETTERS/SETTERS

    def set_location(self, pos):
        if self._location:
            raise Exception("Shoot cannot be overwritten")
        self._location.set_location(pos)

    #OPERATORS OVERLOADERS

    def __iadd__(self, other):
        raise Exception("Shoot cannot be overwritten")
