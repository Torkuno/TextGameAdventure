import item


class Potion(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Potin'
        self._description = 'Drink it to recover health'
