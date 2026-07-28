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
    def key_in_dict(dictionary):
        required_keys = ['name' , 'health', 'strength' , 'agility' , 'luck', 'attack']
        checker = True
        for key in required_keys:
            if key not in dictionary:
                print('missing key' , key, " ", end = " | ")
                checker = False      
        return checker    

    @staticmethod
    def val_key_value(player,monster):
        erorrs_value = []
        if not Validations.is_str(player["name"]):
            erorrs_value.append("The name of player must be a string.")
        if not Validations.is_int_or_flo(player["attack"]):
            erorrs_value.append("The attack of player must be a number.")
        if not Validations.is_int_or_flo(player["health"]):
            erorrs_value.append("The health of player must be a number.")
        if not Validations.is_str(monster["name"]):
            erorrs_value.append("The name of monster must be a string.")
        if not Validations.is_int_or_flo(monster["attack"]):
            erorrs_value.append("The attack of monster must be a number.")
        if not Validations.is_int_or_flo(monster["health"]):
            erorrs_value.append("The health of moster must be a number.")
        
        if erorrs_value == []:
            return True
        else:
            print("config value erorr:")
            for err in erorrs_value:
                print(err)