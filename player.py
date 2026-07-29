from entity import  Entity

class Player(Entity):
    def __init__(self, name, health, strength, agility, luck, attack):
        super().__init__(name, health, strength, agility, luck, attack)
    
    def can_take_potion(self):
        return True
    
    def add_potion(self):
        print("Added a potion to the bag")
        return True