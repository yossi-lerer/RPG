from entity import  Entity

class Player(Entity):
    def __init__(self, name, health, strength, agility, luck, attack):
        super().__init__(name, health, strength, agility, luck, attack)
