__author__ = 'jitrixis'

class Utils:
    FIELD_WIDTH = 10
    FIELD_HEIGHT = 10

    #CLASSMETHODS

    @classmethod
    def str_to_pos(cls, string):
        #DEV
        if type(string) is not str:
            raise TypeError("Type not allowed, string expected")
        if 2 >= len(string) >= 3:
            raise ValueError("Missing characters")
        return ((int(string[1:])-1), (ord(string[0])-64)%32-1)