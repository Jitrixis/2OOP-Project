from battleship.field.field import Field

__author__ = 'jitrixis'


class Player:
    def __init__(self):
        self.__name = None
        self.__field = Field()

    @staticmethod
    def checkName(name):
        if not len(name) <= 20:
            raise ValueError("size exceeded")

    @staticmethod
    def testName(name):
        try:
            Player.checkName(name)
        except ValueError:
            return False
        return True

    def getName(self):
        return self.__name

    def setName(self, name):
        Player.checkName(name)
        self.__name = name
        return self