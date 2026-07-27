from player import Player
from monster import Monster
from entity import Entity

class Battle:
    def __init__(self,player:Player, monster: Monster):
        self.player = player
        self.monster = monster

    def run (self):
        print (
            f""""
            Welcome to the battle between {self.player.name} and monster
            {self.player.name} stats are;
            Life: {self.player.health}
            Strength: {self.player.strength}
            Agility: {self.player.agility}
            Luck: {self.player.luck}

            Monsters stats are;
            Life: {self.monster.health}
            Strength: {self.monster.strength}
            Agility: {self.monster.agility}
            Luck: {self.monster.luck}

        {self.player.name} attacks first
        """)

        counter = 0

        while self.player.health > 0 and self.monster.health > 0:
            if counter % 2 == 0:
                self.attack(self.player,self.monster)
            else:
                self.attack(self.monster,self.player)

            counter += 1
        print ("Game Over")

        if self.player.health == 0:
            print (f"{self.player.name} died, Monster Won!")
        else:
            print (f"Monster died, {self.player.name} Won!")

    def attack (self, attacker: Entity, defender: Entity):

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


