from config import *
class Validations:

    @staticmethod
    def is_str(name):
        return  isinstance(name,str) and name.isalpha()

    @staticmethod
    def is_int_or_flo(num):
        return isinstance(num,(int,float))

    @staticmethod
    def is_instance(instance,cls):
        return isinstance(instance,cls)
    
    @staticmethod
    def validtae_config (player,monster):
        if Validations.is_str(player["name"]):
            if Validations.is_int_or_flo(player["attack"]):
                if Validations.is_int_or_flo(player["health"]):
                    if Validations.is_str(monster["name"]):
                        if Validations.is_int_or_flo(monster["attack"]):
                            if Validations.is_int_or_flo(monster["health"]):
                                return True
                

    @staticmethod
    def key_in_dict(dictionary):
        required_keys = ['name' , 'health', 'strength' , 'agility' , 'luck', 'attack']
        checker = True
        for key in required_keys:
            if key not in dictionary:
                print('missing key' , key, " ", end = " | ")
                checker = False      
        return checker    
