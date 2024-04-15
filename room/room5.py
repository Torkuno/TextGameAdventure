from .room import Room
import entity


class Room5(Room):
    def __init__(self) -> None:
        super().__init__()
        self._description = f'This is room5'

        goblin = entity.Goblin()
        bat = entity.Bat()
        self._room_enemies = [goblin, bat]
