from room import *
from random import *
import config
from monster import *

class Maze:
    def __init__(self, room_count: int):
        self.room_count = room_count
        self.maze = []
        self.monster_chance = config.maze_settings["monster_chance"]
        self.potion_chance = config.maze_settings["potion_chance"]
        
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
            if self.will_be_monster() is Monster():
                self.maze.append (Room (Monster(),))
            elif self.will_be_monster() == True:
                self.maze.append (Room (None,True))
            else:
                self.maze.append (Room ())

    def will_be_monster(self):
        if random.randomint(1, 10) <= self.monster_chance:
            return Monster()
        elif random.randomint(1, 10) <= self.potion_chance:
            return True
        else:
            return 'The room is empty.'