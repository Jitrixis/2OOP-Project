import random
from battleship.interface.utils import Utils

__author__ = 'jitrixis'


class TTY:

    #CLASSMETHODS

    @classmethod
    def cls(cls):
        print('\n'*40)

    @classmethod
    def player_set_name(cls):
        return input("Enter a surname : ")

    @classmethod
    def location_init(cls, xyo=True):
        if xyo:
            return [Utils.str_to_pos(input("Enter case value (A1) : ")), int(input("Enter orientation : "))]
        else:
            return [Utils.str_to_pos(input("Enter case value (A1) : ")), 0]

    @classmethod
    def location_error(cls):
        print("\033[93mLocation incorrect, please enter a new one !\033[0m")

    @classmethod
    def player_show_turn(cls, name):
        print(' '*10+name)
        print('\n'*3)
        input()