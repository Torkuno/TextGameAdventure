from .room import Room
import entity

class Room6(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'This is room6'

        alpha_hound = entity.AlphaHound()
        self._room_enemies = [alpha_hound]
