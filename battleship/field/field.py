__author__ = 'jitrixis'

from battleship.boat.boat import *


class Field:
    def __init__(self):
        self.__boats = (
            BoatAircraftCarrier(),
            BoatBattleShip(),
            BoatCruiser(),
            BoatDestroyer(),
            BoatDestroyer(),
            BoatSubmarine(),
            BoatSubmarine()
        )

    def getBoats(self):
        return self.__boats

    def isBoatsReady(self):
        for boat in self.__boats:
            if not boat.isReady():
                return False
        return True
