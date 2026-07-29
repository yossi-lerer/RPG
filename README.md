- Project name: RPG
- Developers: Yosi Lerr, Doitch, David Kalaora and Yaakov Soibelman,

- Brief description of the game: Role-playing game. A player enters a maze. The maze contains rooms. Each room can contain a monster, a potion, or an empty room. The player does not know what is inside until he enters. The player has the option to choose whether to enter or end the game with a summary.
If there is a monster in the room, a battle takes place between the player and the monster. If the monster wins, the game ends. If the player wins, if this is the last room, a summary of the game will be displayed. If this is not the last room, the player will have the option to enter the next room.
If there is a potion, the player will take the potion if there is room in the bag.
If the room is empty, the game continues as usual.

## Project files:

1. main.py - the main file, which runs the game.
2. battle.py - has class Battle with 2 functions: one that runs the battle and one that registers each attack.
3. entity.py - has class Entity, which constructs the main attributes for every character in the game.
4. player.py - Contains the Player class, which inherits the entity and holds three methods for checking for free space in the bag, adding a potion to the bag, and counting victories.
5. monster.py - has class Monster, which inherits from Entity.
6. config.py - The configuration file contains settings necessary for the game.
7. validations.py - this file validates 7 things:
    1. Checks that there are 3 settings - player_settings and monster_settings maze_settings - these names must be exact!
    2. checks that keys: "name", "health" and "attack" exist in monster and player settings.
    3. checks that values stoared in these keys are correct - "name" value must be str, "health" and "attack" can be either int or float.
    4. Handling an error when writing a variable name that does not exist in the config file.
    5. Dealing with problematic config file import
    6. Check that there are at least 4 rooms in the config file
    7. Checking that there are at least 3 monsters in the maze
8. game.py - receives the maze with the player and manages the process of entering rooms and triggering battles 
9. maze.py - creates a maze with room contents and instantiates a room
10. room.py - holds the contents of the rooms and manages methods for displaying the contents.


## Operating instructions: 

1. Edit the config.py file with your data
    The file should contain two dictionary variables with the names player_settings, maze_settings and one list variables monster_settings

    The player_settings dictionary should contain the following keys and values:

        "name": str, "health": number (int/float), "strength": number(int/float), "agility": number(int/float), "luck": number(int/float), "attack": number(int/float)
        
    The monster_settings list should contain dictionaries of monsters. Each dictionary represents a monster:

    Each dictionary should contain the following keys and values:

            "name": str, "health": number (int/float), "strength": number(int/float), "agility": number(int/float), "luck": number(int/float), "attack": number(int/float)

    The maze_settings dictionary should contain the following keys and values:

            "room_count": int, "monster_chance": int, "potion_chance": int

    For example:

            player_settings = {"name": "mosh", "health": 1000, "strength": 50.5, "agility": 5, "luck": 5, "attack": 20}
            monster_settings = [{"name": "goblin", "health": 80.9, "strength": 50.5, "agility": 5, "luck": 5, "attack": 30}, {"name": "orc", "health": 80.9, "strength": 50.5, "agility": 5, "luck": 5, "attack": 30}]
            maze_settings = {"room_count": 4, "monster_chance": 8, "potion_chance": 5}
                    
    *Without an accurate definition of the config file, the launch will end without the game running.*
   
2. To run the game, run the main file in the terminal.
    For example:

        python main.py

## On run

A welcome message and a short description of the game will be displayed
Then the menu will be displayed with the option to enter the room or end the game
A battle will begin if you enter the room and a battle is underway
At the end of the game a summary message will be displayed