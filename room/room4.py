from .room import Room
import entity
import item

class Room4(Room):
    def __init__(self):
        super().__init__()
        self._description = f'Old weapones covered in rust are on wooden stands, it must be the armory'

        sword = item.Shortsword()
        self._room_items = [sword]

        goblin = entity.Goblin()
        self._room_enemies = [goblin]
