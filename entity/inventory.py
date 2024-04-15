import item

class Inventory:
    def __init__(self) -> None:
        self._content = []

    def add_item(self, item: item.Item):
        self._content.append(item)
        
    def get_items(self):
        return self._content

    def __repr__(self) -> str:
        to_print = ''

        for i in self._content:
            to_print += i.get_name() + ': ' + i.get_description() + '\n'
        
        return to_print