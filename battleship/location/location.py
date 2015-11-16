from battleship.interface.tty import TTY
from battleship.interface.utils import Utils

__author__ = 'jitrixis'

class Location:

    def __init__(self, length=1):
        if type(length) is not int:
            raise ValueError("Length should be an integer")
        if not length > 0:
            raise ValueError("Length should be positive")
        self.__pos = None
        self.__orientation = None
        self.__length = length

    #GETTERS/SETTERS

    def get_pos(self):
        return self.__pos

    def get_orientation(self):
        return self.__orientation

    def __reset_location(self):
        self.__pos = None
        self.__orientation = None

    def set_location(self, pos, orientation=0, constraints=()):
        if self:
            raise Exception("Location cannot be overwritten")
        if type(constraints) is not tuple:
            raise TypeError("Constraints should to be a tuple")
        self.__pos = pos
        self.__orientation = orientation

        self.__check_orientation()
        self.__check_pos()
        self.__check_constraint(constraints)

    def get_points(self):
        list = []
        for i in range(len(self)):
            list.append(self.__getitem__(i))
        return list

    #METHODS

    def __check_orientation(self):
        if type(self.__orientation) is not int:
            raise TypeError("orientation has to be an integer")
        if not 0 <= self.__orientation <= 1:
            raise ValueError(self.__orientation, "is not a valid orientation")

    def __check_pos(self):
        if type(self.__pos) is not tuple:
            raise TypeError("location has to be a tuple")
        if len(self.__pos) != 2:
            raise ValueError("missing values")
        for elem in self.__pos:
            if type(elem) is not int:
                raise ValueError("tuple values are not integers")
        width = Utils.FIELD_WIDTH-self.__length*self.__orientation
        height = Utils.FIELD_HEIGHT-self.__length*(1-self.__orientation)
        if (not 0 <= self.__pos[0] <= width) or (not 0 <= self.__pos[1] <= height):
            raise ValueError("field exceeded")

    def __check_constraint(self, constraints):
        for constraint in constraints:
            if constraint.get_location() in self:
                raise ValueError("Location is in the constraint")

    #VIEWS

    def view_init_location(self, boats=()):
        while not self:
            try:
                inputs = TTY.location_init(xyo=(boats is not ()))
                self.set_location(inputs[0], orientation=inputs[1], constraints=boats)
            except:
                self.__reset_location()
                TTY.location_error()

    #OPERATORS OVERLOADERS

    def __str__(self):
        return str(dict(pos=self.get_pos(), orientation=self.get_orientation(), length=len(self)))

    def __bool__(self):
        try:
            self.__check_orientation()
            self.__check_pos()
        except:
            return False
        return True

    def __len__(self):
        if not self:
            return 0
        return self.__length

    def __getitem__(self, key):
        if key >= len(self):
            raise IndexError()
        return (self.get_pos()[0]+key*self.get_orientation(), self.get_pos()[1]+key*(1-self.get_orientation()))

    def __contains__(self, other):
        return bool(len(set(self.get_points()) & set(other.get_points())))