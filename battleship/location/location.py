__author__ = 'jitrixis'

class Location:
    def __init__(self):
        self.__x = None
        self.__y = None
        self.__orientation = None
        self.__length = None

    def set_pos(self, pos):
        if len(pos) < 2 or len(pos) > 3:
            raise ValueError("missing values")
        self.__x = pos[0]
        self.__y = pos[1]
        if len(pos) == 3:
            self.__orientation = pos[2]
        return self
