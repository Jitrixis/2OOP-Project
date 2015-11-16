from battleship.location.location import Location

__author__ = 'jitrixis'


class Boat:
    def __init__(self):
        try:
            type(self._location)
        except AttributeError:
            self._location = Location()

    #GETTERS/SETTERS

    def get_location(self):
        return self._location

    def set_location(self, pos, orientation, constraints):
        self._location.set_location(pos, orientation=orientation, constraints=constraints)
        return self

    #OPERATORS OVERLOADERS
    def __str__(self):
        return ' '

    def __len__(self):
        return len(self._location)

    def __bool__(self):
        return bool(self._location)

    def __contains__(self, other):
        if not self or not other:
            return False
        return self.get_location() in other.get_location()

    #VIEWS

    def view_set_location(self, boats):
        self._location.view_init_location(boats)


class BoatAircraftCarrier(Boat):
    def __init__(self):
        self._location = Location(5)
        super().__init__()

    def __str__(self):
        return 'A'


class BoatBattleShip(Boat):
    def __init__(self):
        self._location = Location(4)
        super().__init__()

    def __str__(self):
        return 'B'


class BoatCruiser(Boat):
    def __init__(self):
        self._location = Location(3)
        super().__init__()

    def __str__(self):
        return 'C'


class BoatDestroyer(Boat):
    def __init__(self):
        self._location = Location(2)
        super().__init__()

    def __str__(self):
        return 'D'


class BoatSubmarine(Boat):
    def __init__(self):
        self._location = Location(1)
        super().__init__()

    def __str__(self):
        return 'S'