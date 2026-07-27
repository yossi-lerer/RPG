
class entity:
    def __init__(self,name,health,strength,agility,luck):
        self.name=name
        self.health=health
        self.strength=strength
        self.agility=agility
        self.luck=luck
    def say_details(self):
        return f"my name is: {self.name}"   

