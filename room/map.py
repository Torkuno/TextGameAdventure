from .room0 import Room0
from .room1 import Room1
from .room2 import Room2
from .room3 import Room3
from .room4 import Room4
from .room5 import Room5
from .room6 import Room6
from .room7 import Room7
from .room8 import Room8
from .room9 import Room9
from .room10 import Room10
from .room11 import Room11


class Map:
    def __init__(self) -> None:
        self._room0 = Room0()
        self._room1 = Room1()
        self._room2 = Room2()
        self._room3 = Room3()
        self._room4 = Room4()
        self._room5 = Room5()
        self._room6 = Room6()
        self._room7 = Room7()
        self._room8 = Room8()
        self._room9 = Room9()
        self._room10 = Room10()
        self._room11 = Room11()

        self.__room_0_connections()
        self.__room_1_connections()
        self.__room_2_connections()
        self.__room_3_connections()
        self.__room_4_connections()
        self.__room_5_connections()
        self.__room_6_connections()
        self.__room_7_connections()
        self.__room_8_connections()
        self.__room_9_connections()
        self.__room_10_connections()
        self.__room_11_connections()


    def __room_0_connections(self):
        # Room 0 connections
        self._room0.north = self._room9
        self._room0.west = self._room1
        self._room0.south = False
        self._room0.east = self._room7

    def __room_1_connections(self):
        self._room1.north = False
        self._room1.west = self._room2
        self._room1.south = False
        self._room1.east = self._room0

    def __room_2_connections(self):
        self._room2.north = self._room4
        self._room2.west = self._room3
        self._room2.south = False
        self._room2.east = self._room1

    def __room_3_connections(self):
        self._room3.north = self._room5
        self._room3.west = False
        self._room3.south = False
        self._room3.east = self._room2

    def __room_4_connections(self):
        self._room4.north = False
        self._room4.west = self._room5
        self._room4.south = self._room2
        self._room4.east = False

    def __room_5_connections(self):
        self._room5.north = self._room6
        self._room5.west = False
        self._room5.south = self._room3
        self._room5.east = self._room4

    def __room_6_connections(self):
        self._room6.north = False 
        self._room6.west = False
        self._room6.south = self._room5
        self._room6.east = False

    def __room_7_connections(self):
        self._room7.north = self._room8
        self._room7.west = self._room0
        self._room7.south = False
        self._room7.east = False

    def __room_8_connections(self):
        self._room8.north = False
        self._room8.west = False
        self._room8.south = self._room7
        self._room8.east = False

    def __room_9_connections(self):
        self._room9.north = self._room11
        self._room9.west = self._room10
        self._room9.south = self._room0
        self._room9.east = False

    def __room_10_connections(self):
        self._room10.north = False
        self._room10.west = False
        self._room10.south = False
        self._room10.east = self._room9

    def __room_11_connections(self):
        self._room11.north = False
        self._room11.west = False
        self._room11.south = self._room9
        self._room11.east = False

    def get_first_room(self):
        return self._first_room
