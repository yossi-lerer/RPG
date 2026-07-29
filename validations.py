from monster import Monster
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
    def key_in_dict(dictionary, required_keys):
        checker = True
        for key in required_keys:
            if key not in dictionary:
                print('missing key:' , key, "in config file ", end = " | ")
                checker = False      
        return checker

    @staticmethod
    def val_key_value(player,monster,maze):
        erorrs_value = []
        if not Validations.is_str(player["name"]):
            erorrs_value.append("The name of player must be a string.")
        if not Validations.is_int_or_flo(player["attack"]):
            erorrs_value.append("The attack of player must be a number.")
        if not Validations.is_int_or_flo(player["health"]):
            erorrs_value.append("The health of player must be a number.")
        if not isinstance(maze["room_count"], int):
            erorrs_value.append("The room_count of maze must be a integer.")
        if not isinstance(maze["monster_chance"], int):
            erorrs_value.append("The monster_chance of maze must be a integer.")
        if not isinstance(maze["potion_chance"], int):
            erorrs_value.append("The potion_chance of maze must be a integer.")
        for _ in range(2):
            if not Validations.is_str(monster[_]["name"]):
                erorrs_value.append("The name of monster must be a string.")
            if not Validations.is_int_or_flo(monster[_]["attack"]):
                erorrs_value.append("The attack of monster must be a number.")
            if not Validations.is_int_or_flo(monster[_]["health"]):
                erorrs_value.append("The health of moster must be a number.")    
        if erorrs_value == []:
            return True
        else:
            print("config value erorr:")
            for err in erorrs_value:
                print(err)
            exit()

    @staticmethod
    def val_import_config():
        try:
            from config import player_settings, monster_settings, maze_settings
        except ImportError:
            print("The config file is missing one or more of the variables player_settings, monster_settings, maze_settings")
            print ("Fix and run game again")
            exit()
        except NameError:
            print("In the config.py file, keys or values ​​are used with text without quotes")
            print ("Fix and run game again")
            exit()
    
    @staticmethod
    def val_key_and_value(player_settings, monster_settings, maze_settings):
        required_keys_monster_and_players = ['name' , 'health', 'strength' , 'agility' , 'luck', 'attack']
        required_keys_maze_settings = ['room_count', 'monster_chance', 'potion_chance']
        if Validations.key_in_dict(player_settings, required_keys_monster_and_players) and Validations.key_in_dict(monster_settings[0], required_keys_monster_and_players) and Validations.key_in_dict(monster_settings[1], required_keys_monster_and_players) and Validations.key_in_dict(maze_settings, required_keys_maze_settings):
            if Validations.val_key_value(player_settings,monster_settings,maze_settings):
                return True
        else:
            print ("Fix and run game again")
            exit()

    @staticmethod
    def val_min_rooms(room_count):
        if room_count < 4:
            print("Minimum room_count must be less than 4")
            print ("Fix and run game again")
            exit()

    @staticmethod
    def validate_monsters(maze):
        count = 0
        for room in maze :
            if room.has_monster():
                count += 1
        if count < 3:
            return False 
        else:
            return True