from entity import *
from furniture import Merchant


class Game:
    def __init__(self) -> None:
        print("========== intro ==========")
        print('You can use the following commands to interact with the game')
        print()
        self.help()
        print("===========================")
        print()

        # allow the game loop to be broken
        self._is_running = True

        # set the player name
        self._p_name = input('Enter your player name: ')
        self._p_name = str(f"\033[0;34m{self._p_name}\033[0m")

        print()
        print(f'You are {self._p_name}.')
        print('You are in a dungeon trying to recover a specific item.')
        print('Explore at your own risk in this place!')
        print("===========================")
        print()

        # create the player instance
        self._player = Player(self._p_name)

        # run the game loop
        self.game_loop()

    def game_loop(self):
        while self._is_running:
            self.player_input()

            if self._player.get_room()._room_enemies:
                battle(self._player, self._player.get_room()._room_enemies)


    def player_input(self):
        print('=' * 27)
        pl_in = input('What do you want to do: ')

        arg_list = pl_in.split(maxsplit=1)
        commande = arg_list[0]

        if commande == 'go':
            if len(arg_list) != 2: # error handeling for no argument after <go>
                print('wrong input')
                return

            direction = arg_list[1]

            if direction not in ['north', 'east', 'south', 'west']:
                print("this direction doesn't exist")
                print('only: north, east, south, west can be used')
                return

            self._player.move(direction)

        elif commande == 'heal':  # use a potion in the inventory to heal the player
            pass

        elif commande == 'look':  # repeat the description of the surounding
            self._player.look()

        elif commande == 'inventory':  # show the content of the inventory
            self._player.list_inventory()

        elif commande == 'interact':
            if len(arg_list) != 2:  # error handeling for no argument after <interact>
                print('wrong input')
                return

            item = arg_list[1].lower()

            for i in self._player.get_room().get_items():
                if item == str(i).lower():
                    self._player.interact(i)
                    return

            print(f'{item} is not in the room.')
        
        elif commande == 'quit':
            exit()

        elif commande == 'help':
            self.help

        else:
            print('wrong input')
    
    def help(self):
        print('<go> <north|east|south|west>\tMove the player in the selected direction')
        print('<look>\t\t\t\tGive an accurate description of the room')
        print('<inventory>\t\t\tDisplay the content of the inventory')
        print('<interact> <object name>\tTake the item and interact with things')
        print('<quit>\t\t\t\tQuit the game')
        print('<help>\t\t\t\tDisplay this help')


Game()


