import item


class CoinPouch(item.Item):
    def __init__(self) -> None:
        super().__init__()

        self._name = 'Coin pouch'
        self._description = 'A pouch full of spiders... NO! of coins obviously!'
