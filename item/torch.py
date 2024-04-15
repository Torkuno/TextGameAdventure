import item


class Torch(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Torch'
        self._description = 'Illuminate the dark with a bright yellow ligth.'
