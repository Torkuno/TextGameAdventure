from .room import Room


class Room0(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = 'This is the beginig room. It is empty.'
