from player import Player
from monster import Monster
from battle import Battle
from validations import Validations
from config import *
from maze import *
from game import *

Validations.val_import_config()
Validations.val_key_and_value(player_settings, monster_settings, maze_settings)
Validations.val_min_rooms(maze_settings["room_count"])

player = Player(player_settings["name"], player_settings["health"], player_settings["strength"], player_settings["agility"], player_settings["luck"], player_settings["attack"])
maze = Maze(maze_settings["room_count"])
maze.generate()
game = Game(player,maze)
game.run()