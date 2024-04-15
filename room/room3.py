from .room import Room
import entity
import item

class Room3(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'Multiples armors are standing in holes carved in the walls'

        roundshield = item.RoundShield()
        self._room_items = [roundshield]


        bat_1 = entity.Bat()
        bat_2 = entity.Bat()
        self._room_enemies = [bat_1, bat_2]
