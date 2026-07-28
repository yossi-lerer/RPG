from player import Player
from monster import Monster
from entity import Entity
import sys

class Battle:
    def __init__(self,player:Player, monster: Monster):
        self.player = player
        self.monster = monster

    def run (self):
        skull = "\U0001F480"
        trophy = "\U0001F3C6"
        crossed_swords = "\u2694\ufe0f"
        explosion = "\U0001F4A5"
        knight = "\U0001F3C7" 
        monster_ogre   = "\U0001F479"
        print (
            f""""
            Welcome to the battle between {self.player.name}{knight} and {self.monster.name}{monster_ogre}

            {crossed_swords}

            {self.player.name} {knight} stats are;
            Life: {self.player.health}
            Strength: {self.player.strength}
            Agility: {self.player.agility}
            Luck: {self.player.luck}

            {self.monster.name} {monster_ogre} stats are;
            Life: {self.monster.health}
            Strength: {self.monster.strength}
            Agility: {self.monster.agility}
            Luck: {self.monster.luck}

        {self.player.name} {knight} attacks first
        """)

        counter = 0

        while self.player.health > 0 and self.monster.health > 0:
            if counter % 2 == 0:
                self.attack(self.player)
                print (f"{self.player.name} {knight} attacked {explosion}")
            else:
                self.attack(self.monster)
                print (f"{self.monster.name} {monster_ogre} attacked {explosion}")

            counter += 1
            
        print ("Game Over")

        if self.player.health == 0:
            print (f"{self.player.name} {knight} died {skull}, {self.monster.name} {monster_ogre} Won! {trophy}")
        else:
            print (f"{self.monster.name} {monster_ogre} died {skull}, {self.player.name} {knight} Won! {trophy}")

    def attack (self, attacker: Entity):

        if isinstance(attacker, Monster):
            if self.monster.attack <= self.player.health:
                self.player.health -= self.monster.attack
            else:
                self.player.health = 0
                
        else:
            if self.player.attack <= self.monster.health:
                self.monster.health -= self.player.attack
            else:
                self.monster.health = 0