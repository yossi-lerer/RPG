- Project name: RPG
- Developers: Yosi Lerr, Doitch, David Kalaora Yaakov Soibelman,

- Short game description: An RPG game. A player - "mosh" - enters a battle with a monster - "mon".
mosh begins and attacks mon, then mon attacks mosh. This cycle repeats until one of them "dies" - until their health is reduced to 0.

## Project files & description:
    1. main.py - the main file, which runs the game.
    2. battle.py - has class Battle with 2 functions: one that runs the battle and one that registers each attack.
    3. entity.py - has class Entity, which constructs the main attributes for every character in the game.
    4. player.py - has class Player, which inherits from Entity.
    5. monster.py - has class Monster, which inherits from Entity.
    6. config.py - config file has a dictionary which stores all set values of players and game.
    7. validations.py - this file validates 2 things: 1. Checks that the keys: "name", "health" and "attack" exist in monster and player. 2. checks that values stoared in these keys are correct - valid.

- Both characters have a few attributes whose values are set in a config file. These include: health, attack, agility, luck, strength, name.

## Operating instructions: 
    1. Edit the config.py file with your data
        The file should contain two dictionary variables with the names player_settings, monster_settings
        Each dictionary should contain the following keys and values:
        ```
        "name": str, "health": number, "strength": number, "agility": number, "luck": number, "attack": number
        ```
        For example:
        ```
        player_settings = {"name": "mosh", "health": 80.9, "strength": 50.5, "agility": 5, "luck": 5, "attack": 20}
        monster_settings = {"name": "mon", "health": 80.9, "strength": 50.5, "agility": 5, "luck": 5, "attack": 30}
        ```
        *Without an accurate definition of the config file, the game will not run.*
    2. To run the game, run the main file in the terminal.
        For example:
       ```
        python main.py
       ```

## On run
 a welcome message and a character status chart will be shown on the terminal. As the game runs, the terminal will show each time a character attacks another one. Once a player's health reaches 0, the terminal will print "Game Over" and who won the game.