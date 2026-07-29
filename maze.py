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



    