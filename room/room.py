from entity import *
from item import Torch, Scroll
from furniture import Merchant


class Room:
    def __init__(self) -> None:
        # description of the room
        self._description = "Fake description"
        self._alt_description = 'alternated description'

        # item condition
        self._is_dark = False

        # possibles connection to other roomes
        self.north = False
        self.east = False
        self.south = False
        self.west = False

        # item in the room
        self._room_items = []

        # enemies in the room
        self._room_enemies = []

    # return the north connection (False if none)
    def go_north(self):
        return self.north

    # return the east connection (False if none)
    def go_east(self):
        return self.east

    # return the south connection (False if none)
    def go_south(self):
        return self.south

    # return the west connection (False if none)
    def go_west(self):
        return self.west

    # function triggered when the player enter the room
    def player_enter(self):
        print('You can go:')
        if self.north:
            print('North  ', end='')
        if self.east:
            print('east  ', end='')
        if self.south:
            print('south  ', end='')
        if self.west:
            print('west  ', end='')

        print()

        print(self._description)


    # print the description of the room
    def print_description(self):
        print(self._description)
        if self._room_items:
            print('you can see the following:')
            for i in self._room_items:
                print(i)
            print('in the room')

    # check the player inventory for relevent item for the room
    def check_unlock_items(self, pl_inv: Inventory):
        for item in pl_inv.get_items():
            if isinstance(item, Torch) and self._is_dark:
                self._is_dark = False
                self.update_description()

    # update the description of the room to the alternate description
    def update_description(self):
        self._description = self._alt_description

    # return a list of everything that is in the room
    def get_items(self):
        return self._room_items

    # remove an item in the room item list
    def remove_item(self, item):
        for i in self._room_items:
            if str(item).lower == str(i).lower:
                self._room_items.remove(item)