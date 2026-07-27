from config import player_settigs, monster_settigs
from player import Player
from monster import Monster
from battle import Battle

player = Player(player_settigs["name"], player_settigs["health"], player_settigs["strength"], player_settigs["agility"], player_settigs["luck"], player_settigs["attack"])
monster = Monster(monster_settigs["name"], monster_settigs["health"], monster_settigs["strength"], monster_settigs["agility"], monster_settigs["luck"], monster_settigs["attack"])
battle = Battle(player, monster)
battle.run()