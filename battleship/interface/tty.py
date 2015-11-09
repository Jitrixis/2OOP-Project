from battleship.utils.utils import Utils

__author__ = 'jitrixis'


class TTY:
    @staticmethod
    def player_set_name():
        return input("Enter a surname : ")

    @staticmethod
    def boat_set_location():
        return Utils.to_location(eval(input("Enter (x) value : ")),
                                 eval(input("Enter (y) value : ")),
                                 eval(input("Enter (o) value : ")))
