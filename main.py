try:
    from config import player_settings, monster_settings
except ImportError:
    print("The config file is missing one or more of the variables player_settings, monster_settings")
    exit()
from player import Player
from monster import Monster
from battle import Battle
from validations import Validations

if Validations.key_in_dict(player_settings) and (monster_settings):
    if Validations.val_key_value(player_settings,monster_settings):
        player = Player(player_settings["name"], player_settings["health"], player_settings["strength"], player_settings["agility"], player_settings["luck"], player_settings["attack"])
        monster = Monster(monster_settings["name"], monster_settings["health"], monster_settings["strength"], monster_settings["agility"], monster_settings["luck"], monster_settings["attack"])
        battle = Battle(player, monster)
        battle.run()
    else:
        print ("something is wrong, game exiting")