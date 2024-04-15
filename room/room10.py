from .room import Room


class Room10(Room):
    def __init__(self) -> None:
        super().__init__()

        self._is_dark = True

        self._description = 'This room is very dark.'
        self._alt_description = 'Thanks to your torch you can see in this dark room. You can only go east.'