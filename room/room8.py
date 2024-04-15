from .room import Room


class Room8(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'This is room8'
