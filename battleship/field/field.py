from battleship.boat.boat import *
from battleship.shoot.shoot import *

__author__ = 'jitrixis'



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
        self.__shootFired = []
        self.__shootEnemy = []

    def get_shoot_fired(self):
        return self.__shootFired

    def add_shoot_fired(self, shoot):
        if not self.is_boats_ready():
            raise Exception("Boats are not ready")
        self.__shootFired.append(shoot)
        return shoot

    def get_shoot_enemy(self):
        return self.__shootEnemy

    def add_shoot_enemy(self, shoot):
        if not self.is_boats_ready():
            raise Exception("Boats are not ready")
        shoot += self.__fetch_boats(shoot)
        self.__shootEnemy.append(shoot)
        return shoot

    def get_boats(self):
        return self.__boats

    def is_boats_ready(self):
        for boat in self.__boats:
            if not boat.is_ready():
                return False
        return True

    def __fetch_boats(self, shoot):
        for boat in self.__boats:
            if boat.in_location(shoot.get_location()):
                return ShootSuccessful()
        return ShootFailed()

    def visual_set_boats(self):
        for boat in self.__boats:
            self.visual_get_boats()
            boat.visual_set_location()

    def visual_get_boats(self):
        print("SHOW BOATS")