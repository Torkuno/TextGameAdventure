from .room import Room
from item import Torch, Scroll

class Room1(Room):
    def __init__(self) -> None:
        super().__init__()
        self._room_items = [Torch(), Scroll()]
        self._description = f'This room seem to be an ancient library. A lot of paper and book is spoiled by time.'
