from entity import Entity

class Monster(Entity):
    def __init__(self, name, health, strength, agility, luck):
        super().__init__(name, health, strength, agility, luck)