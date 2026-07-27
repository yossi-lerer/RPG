
class Entity:
    def __init__(self,name,health,strength,agility,luck, attack):
        self.name=name
        self.health=health
        self.strength=strength
        self.agility=agility
        self.luck=luck
        self.attack = attack
    def say_details(self):
        return f"my name is: {self.name}"   
    def is_alive(self):
        return  True if self.health>0 else False

