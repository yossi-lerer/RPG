from player import *
from room import *
from battle import *
from maze import Maze
from config import *

class Game:
    def __init__(self,player: Player, maze: Maze):
        self.player=player
        self.maze=maze
        self.current_room_index=0

    def run(self):
        while self.player.is_alive() and self.current_room_index < self.maze.room_count:
            choice = self.show_main_menu()
            if choice == "1":
                self.enter_next_room()
            elif choice == "2":
                self.show_summary()
                break
            else:
                print("please enter 1 or 2\n")
        if not self.player.is_alive():
            self.show_summary()
        elif self.current_room_index == self.maze.room_count:
            self.show_summary()
        
    def show_main_menu(self):
        user_choose=input(f"\n  >>>menu<<<\nyour next room is:{self.current_room_index+1}\nchoose an option \n 1. enter next room🚪 \n 2. leave game🏃‍♂️‍➡️\n")
        return user_choose

    def enter_next_room(self):
        room = self.maze.get_room(self.current_room_index)
        if room.has_monster():
            battle = Battle(self.player, room.monster)
            battle.run()

        elif room.has_potion:
            if self.player.can_take_potion():
                room.take_potion()
                self.player.add_potion()
        else:
            print("the room is empty\n")
        self.current_room_index += 1

    def show_summary(self):
        knight = "\U0001F3C7"
        print(f"""{self.player.name} {knight} stats are;
Life: {self.player.health}
Strength: {self.player.strength}
Agility: {self.player.agility}
Luck: {self.player.luck}
rooms comleted: {self.current_room_index} out of {maze_settings["room_count"]}✅
you defeated: {self.player.wictories} monsters 👏
""")



        

