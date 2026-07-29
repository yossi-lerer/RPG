from entity import  Entity

class Player(Entity):
    def __init__(self, name, health, strength, agility, luck, attack):
        super().__init__(name, health, strength, agility, luck, attack)
        self.potion = 0
    
    def can_take_potion(self):
        if self.potion < 2:
            return True
        else:
            return False

    
    def add_potion(self):
        self.potion += 1