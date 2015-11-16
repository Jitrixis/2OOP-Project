import copy
from battleship.boat.boat import *
from battleship.interface.tty import TTY
from battleship.interface.utils import Utils
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

    #GETTERS/SETTERS

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
        shoot += Field.__fetch_shoot_boats(shoot, self.__boats)
        self.__shootEnemy.append(shoot)
        return shoot

    def get_boats(self):
        return self.__boats

    def is_boats_ready(self):
        for boat in self.__boats:
            if not boat:
                return False
        return True

    #METHODS
    @classmethod
    def __fetch_shoot_boats(cls, shoot, boats):
        for boat in boats:
            if boat in shoot:
                return ShootSuccessful()
        return ShootFailed()

    #VIEWS

    def view_set_boats(self):
        for boat in self.__boats:
            self.view_get_boats()
            boat.view_set_location(copy.deepcopy(self.__boats))

    def view_get_boats(self):
        TTY.cls()
        friend = [[' ']*Utils.FIELD_WIDTH for _ in range(Utils.FIELD_HEIGHT)]
        enemy = [[' ']*Utils.FIELD_WIDTH for _ in range(Utils.FIELD_HEIGHT)]
        for boat in self.__boats:
            if boat:
                for point in boat.get_location():
                    friend[point[0]][point[1]] = str(boat)
        for shoot in self.__shootEnemy:
            if shoot.get_status():
                for point in shoot.get_location():
                    friend[point[0]][point[1]] = '\033[93m'+friend[point[0]][point[1]]+'\033[0m'
            else:
                for point in shoot.get_location():
                    friend[point[0]][point[1]] = '@'
        for shoot in self.__shootFired:
            if shoot.get_status():
                for point in shoot.get_location():
                    enemy[point[0]][point[1]] = '\033[93mX\033[0m'
            else:
                for point in shoot.get_location():
                    enemy[point[0]][point[1]] = '@'


        print('FRIEND')
        print(end='   ')
        for i in range(10):
            print(chr(65+i), end=' ')
        print()
        for i in range(len(friend)):
            print(i+1, end=' |')
            for j in range(len(friend[i])):
                print(friend[i][j], end='|')
            print()
        print()
        print('ENEMY')
        print(end='   ')
        for i in range(10):
            print(chr(65+i), end=' ')
        print()
        for i in range(len(enemy)):
            print(i+1, end=' |')
            for j in range(len(enemy[i])):
                print(enemy[i][j], end='|')
            print()
        print()