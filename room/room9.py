from .room import Room


class Room9(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'This is room9'
