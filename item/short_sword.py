import item


class Shortsword(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Shortsword'
        self._description = 'A classic shortsword to stab and slash.'
