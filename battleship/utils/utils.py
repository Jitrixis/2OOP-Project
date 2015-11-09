__author__ = 'jitrixis'

class Utils:
    FIELD_WIDTH = 10
    FIELD_HEIGHT = 10

    @staticmethod
    def check_location(location):
        if type(location) is not tuple:
            raise TypeError("location is not a tuple")
        if len(location) != 3:
            raise ValueError("missing values")
        for elem in location:
            if type(elem) is not int:
                raise ValueError("values are not integers")
        if (not 0 <= location[0] < Utils.FIELD_WIDTH) or (not 0 <= location[1] < Utils.FIELD_HEIGHT):
            raise ValueError("field exceeded")
        if not 0 <= location[2] <= 1:
            raise ValueError("not an orientation")

    @staticmethod
    def test_location(location):
        try:
            Utils.check_location(location)
        except (TypeError, ValueError):
            return False
        return True

    @staticmethod
    def to_location(x, y, o):
        location = (x, y, o)
        if not Utils.test_location(location):
            return False
        return location