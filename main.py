from config import player_settigs, monster_settigs
from player import Player
from monster import Monster
from battle import Battle
from validations import Validations

if Validations.key_in_dict(player_settigs) and (monster_settigs):
    
    if Validations.val_key_value(player_settigs,monster_settigs):
        player = Player(player_settigs["name"], player_settigs["health"], player_settigs["strength"], player_settigs["agility"], player_settigs["luck"], player_settigs["attack"])
        monster = Monster(monster_settigs["name"], monster_settigs["health"], monster_settigs["strength"], monster_settigs["agility"], monster_settigs["luck"], monster_settigs["attack"])
        battle = Battle(player, monster)
        battle.run()
    else:
        print ("something is wrong, game exiting")
