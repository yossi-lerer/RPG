from entity import entity

class player(entity):
    def __init__(self, name, health, strength, agility, luck):
        super().__init__(name, health, strength, agility, luck)