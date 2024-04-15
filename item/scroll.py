import item


class Scroll(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Scroll'
        self._description = 'Give you a better instinct of your surrounding'
