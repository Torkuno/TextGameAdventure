import item


class RoundShield(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Round shield'
        self._description = '"Best defence is a good offense." ― Dead people'
