from room import Map
from item import Item
from furniture import Merchant

from .inventory import Inventory
from .entity import Entity

class Player(Entity):
    def __init__(self, name="player"):
        super().__init__(name, 30, 5)
        self._map = Map()
        
        self._room = self._map._room0
        self._room.player_enter()
        self._name = name
        self._inventory = Inventory()

    # define the player movement.
    # is triggered by the <go> commande
    def move(self, direction: str):
        
        # if exist set the current room to the one that is linked to the direction        
        if direction == 'north' and self._room.go_north():
                self._room = self._room.go_north()

        elif direction == 'east' and self._room.go_east():
                self._room = self._room.go_east()

        elif direction == 'south' and self._room.go_south():
                self._room = self._room.go_south()

        elif direction == 'west' and self._room.go_west():
                self._room = self._room.go_west()
        else:
            print('You cannot go in that direction.')
            return

        self._room.check_unlock_items(self._inventory)
        self._room.player_enter()

    def add_item(self, item: Item):
        self._inventory.add_item(item)
        
    def get_room(self):
        return self._room
    
    def list_inventory(self):
        print('Your inventory containe:')
        print(self._inventory)

    def interact(self, item):
        if isinstance(item, Merchant):
            item.player_interaction(self._name)
        
        elif isinstance(item, Item):
            print(f'You took the {item}')
            self._inventory.add_item(item)
            self._room.remove_item(item)

    def heal():
        pass
    

    def look(self):
        if self._room._is_dark:
            print('The room is too dark to see')
            return
        self._room().print_description()