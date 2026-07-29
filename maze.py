from room import *
import random
from config import *
from monster import *
from monster import *

class Maze:
    def __init__(self, room_count: int):
        self.room_count = room_count
        self.maze = []
        self.monster_chance = maze_settings["monster_chance"]
        self.potion_chance = maze_settings["potion_chance"]
        
    def get_room (self, index:int):
        if index <= self.room_count:
            return self.maze[index-1]

    def get_monster_count (self):
        counter = 0
        for i in range (self.room_count):
            if Room.has_monster(self.maze[i]):
                counter +=1
        return counter

    def generate (self):
        for _ in range (self.room_count):
            create_room_content = self.will_be_monster()
            if create_room_content is Monster:
                self.maze.append (Room (create_room_content(),))
            elif create_room_content == True:
                self.maze.append (Room (None,True))
            else:
                self.maze.append (Room (None))

    def will_be_monster(self):
        monster = Monster(monster_settings["name"], monster_settings["health"], monster_settings["strength"], monster_settings["agility"], monster_settings["luck"], monster_settings["attack"])
        if random.randint(1, 10) <= self.monster_chance:
            return monster
        elif random.randint(1, 10) <= self.potion_chance:
            return True
        else:
            return 'The room is empty.'