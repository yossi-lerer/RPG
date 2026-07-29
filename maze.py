from room import *
class Maze:
    def __init__(self, room_count: int):
        self.room_count = room_count
        self.maze = []
        

    def get_room (self, index:int):
        if index <= self.room_count:
            return self.maze[index-1]

    def get_monster_count (self):
        counter = 0
        for i in range (self.room_count):
            if Room.has_monster(self.maze[i]):
                counter +=1
        return counter



    
from random import *
import config

class Maze:
    def __init__(self):
        pass


class ChanceManeger:
    def __init__(self):
        self.monster_chance = config.maze_settings["monster_chance"]
        self.potion_chance = config.maze_settings["potion_chance"]

    def meeting_maneger(self):
        if random.randomint(1, 10) <= self.monster_chance:
            monster_name = config.monster_settings['name']
            return (f'{monster_name} is here !!!')
        
        elif random.randomint(1, 10) <= self.potion_chance:
            return 'There is a potion in this room'

        else:
            return 'The room is empty.'



