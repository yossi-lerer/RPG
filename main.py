from player import Player
from monster import Monster
from battle import Battle
from validations import Validations
Validations.val_import_config()
from config import player_settings, monster_settings, maze_settings
Validations.val_key_and_value(player_settings, monster_settings, maze_settings)
Validations.val_min_rooms(maze_settings["room_count"])

player = Player(player_settings["name"], player_settings["health"], player_settings["strength"], player_settings["agility"], player_settings["luck"], player_settings["attack"])
monster = Monster(monster_settings["name"], monster_settings["health"], monster_settings["strength"], monster_settings["agility"], monster_settings["luck"], monster_settings["attack"])
battle = Battle(player, monster)
battle.run()