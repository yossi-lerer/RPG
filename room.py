class Room:
    def __init__(self, monster: Monster | None , has_potion: bool = False):
        self.monster = monster
        self.has_potion = has_potion

    def has_monster(self):
        if self.monster:
            return True

    def take_potion(self):
        if self.has_potion == False:
            print ("there is no potion available in this room")
        elif self.has_potion == True:
            self.has_potion = False
            print ("potion taken from room")