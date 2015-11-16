from battleship.field.field import Field
from battleship.interface.tty import TTY
from battleship.shoot.shoot import Shoot

__author__ = 'jitrixis'


class Player:
    def __init__(self):
        self.__name = None
        self.__field = Field()

    #GETTER/SETTER

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
        return self

    #METHODS

    def attack(self, player):
        self.view_show_turn()
        self.__field.view_get_boats()
        shoot = Shoot()
        shoot.view_set_location()
        self.__field.add_shoot_fired(player.defense(shoot))


    def defense(self, shoot):
        return self.__field.add_shoot_enemy(shoot)

    #VIEWS

    def view_set_field(self):
        self.__field.view_set_boats()

    def view_set_name(self):
        self.setName(TTY.player_set_name())

    def view_show_turn(self):
        TTY.player_show_turn(self.__name)