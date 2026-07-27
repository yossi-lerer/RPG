from abc import ABC, abstractmethod

class entity(ABC):
    def __init__(self,name,health,strength,agility,luck):
        self.name=name
        self.health=health
        self.strength=strength
        self.agility=agility
        self.luck=luck
    @abstractmethod
    def atteck(self):
        

