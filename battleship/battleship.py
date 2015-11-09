from battleship.player.player import Player

__author__ = 'jitrixis'


class BattleShip:
    def __init__(self):
        self.__players = (Player(), Player())
        self.__players[0].visual_set_name()
        self.__players[0].visual_set_field()
        self.__players[1].visual_set_name()
        self.__players[1].visual_set_field()
        self.__players[0].attack(self.__players[1])