from battleship.field.field import Field
from battleship.interface.tty import TTY
from battleship.shoot.shoot import Shoot
from battleship.utils.utils import Utils

__author__ = 'jitrixis'


class Player:
    def __init__(self):
        self.__name = None
        self.__field = Field()

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        return self

    def visual_set_name(self):
        self.setName(TTY.player_set_name())

    def visual_set_field(self):
        self.__field.visual_set_boats()

    def attack(self, player):
        self.__field.visual_get_boats()
        shoot = Shoot()
        shoot.visual_set_location()
        self.__field.add_shoot_fired(player.defense(shoot))

    def defense(self, shoot):
        return self.__field.add_shoot_enemy(shoot)