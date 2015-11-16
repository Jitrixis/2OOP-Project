from battleship.interface.tty import TTY
from battleship.player.player import Player

__author__ = 'jitrixis'


class BattleShip:
    def __init__(self):
        self.__players = (Player(), Player())

        TTY.cls()
        TTY.player_show_turn('PLAYER 1')
        self.__players[0].view_set_name()
        self.__players[0].view_set_field()

        TTY.cls()
        TTY.player_show_turn('PLAYER 2')
        self.__players[1].view_set_name()
        self.__players[1].view_set_field()

        TTY.cls()
        while True:
            self.__players[0].attack(self.__players[1])
            self.__players[1].attack(self.__players[0])