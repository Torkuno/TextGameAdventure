from .room import Room
from furniture import Merchant

class Room2(Room):
    def __init__(self) -> None:
        super().__init__()
        
        self._description = 'In the center of the room you can see a kobold with a smile. "Welcome to my humble shop" say the kobold'
        _merchant = Merchant()
        self._room_items = [_merchant]