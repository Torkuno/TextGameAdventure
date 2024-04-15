class Item:
    def __init__(self) -> None:
        self._name = 'item'
        self._description = 'generic item description'

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def __repr__(self) -> str:
        return self._name
