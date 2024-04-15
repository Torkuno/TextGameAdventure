from .room import Room


class Room11(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'This is room11'
