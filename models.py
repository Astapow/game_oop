"""
this models contains workhorse
"""
import random

import exceptions
import settings


class Enemy:
    """
    this class is responsible for the work of your opponent
    """

    def __init__(self, level):
        """
        :param level: -> lvl enemy_obj
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        you need to get a random number from 1 to 3
        """
        return random.randint(1, 3)

    def decrease_lives(self):
        """
        with each successful attack of the player, the enemy loses lives
        """
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDownExeption


class Player:
    """
    this class -> input player
    and have any funk -> fight, decrease_lives, attack, defense.
    """

    def __init__(self, name, game_mode):
        """
        :param name: -> input
        """
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0
        self.allowed_attacks = settings.ALLOWED_ATTACKS
        self.game_mode = game_mode

    @staticmethod
    def fight(attack, defense):
        """
        (1) Mage
        (2) Warrior
        (3) Robber
        Mage > Warrior > Robber > Mage
        """
        if attack == defense:
            return 0
        if (attack == settings.MAG and defense == settings.WARRIOR) \
                or (attack == settings.WARRIOR and defense == settings.ROBBER) \
                or (attack == settings.ROBBER and defense == settings.MAG):
            return 1

        return -1

    def decrease_lives(self):
        """
        with every failed defense you lose lives
        """
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.GameOverExeption(self.name, self.score, self.game_mode)

    def attack(self, enemy_obj):
        """
        :param enemy_obj: -> class Enemy

        enemy_defense -> with each successful attack of the player, the enemy loses lives
        player_attack -> input
        while -> validate input
        result -> fight method mechanics

        :return:
        """
        enemy_defense = str(enemy_obj.select_attack())
        player_attack = str(input("Choose your attack: "
                                  "(1) Mage, (2) Warrior, (3) Robber\n"))

        while player_attack not in self.allowed_attacks:
            player_attack = str(input("Invalid input! "
                                      "Choose your attack:"
                                      " (1) Mage, (2) Warrior, (3) Robber\n"))

        print(f"{self.name} attacked with {player_attack}!")
        print(f"Enemy attacked: {enemy_defense}")
        result = self.fight(player_attack, enemy_defense)

        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        else:
            print("You missed!")

    def defense(self, enemy_obj):
        """
        :param enemy_obj: -> class Enemy

        enemy_attack -> with every failed defense you lose lives
        player_defense -> input
        while -> validate input
        result -> fight method mechanics
        :return:
        """
        enemy_attack = str(enemy_obj.select_attack())
        player_defense = str(input("Choose your attack: "
                                   "(1) Mage, (2) Warrior, (3) Robber\n"))

        while player_defense not in self.allowed_attacks:
            player_defense = str(input("Invalid input! Choose your attack: "
                                       "(1) Mage, (2) Warrior, (3) Robber\n"))

        print(f"{self.name} defensed with {player_defense}!")
        print(f"Enemy attacked: {enemy_attack}")
        result = self.fight(enemy_attack, player_defense)

        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You defended successfully!")
        else:
            print("You failed to defend!")
            self.decrease_lives()
            print(f"You have lives left: ===> {self.lives}")

    @staticmethod
    def game_commands(start) -> str:
        """
        this game menu is needed to start the game
        add new param normal/hard
        :param start: -> start in lover case
        """
        if start.lower() == "start":
            return start.lower()
        if start.lower() == "help":
            print(' | '.join(settings.COMMANDS))
            return start.lower()
        if start.lower() == "show scores":
            with open("scores.txt", encoding="utf-8") as file_txt:
                for line in file_txt:
                    print(line)
                return start.lower()
        if start.lower() == "exit":
            raise SystemExit


class HardPlayer(Player):
    """
    this class does the same as the Player class
    """

    def attack(self, enemy_obj):

        """
        it a HARD mode
                :param enemy_obj: -> class Enemy

                enemy_defense -> with each successful attack of the player, the enemy loses lives
                player_attack -> input
                while -> validate input
                result -> fight method mechanics

                :return:
                """

        enemy_defense = str(enemy_obj.select_attack())
        player_attack = str(input("Choose your attack: "
                                  "(1) Mage, (2) Warrior, (3) Robber\n"))

        while player_attack not in self.allowed_attacks:
            player_attack = str(input("Invalid input! "
                                      "Choose your attack:"
                                      " (1) Mage, (2) Warrior, (3) Robber\n"))

        print(f"{self.name} attacked with {player_attack}!")
        print(f"Enemy attacked: {enemy_defense}")
        result = self.fight(player_attack, enemy_defense)

        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1 * settings.N
        else:
            print("You missed!")


class HardEnemy(Enemy):
    """
    this class does the same as the Enemy class
    """

    def __init__(self, level):
        super().__init__(level)
        self.lives = level * settings.N
