"""
we need to import all exceptions for our program
and 'workhorses'
"""
import exceptions
import models
import settings


def play():
    """
    name -> input player
    lvl = start with 1
    input -> name, game mod, start or help, play
    """

    level = 1
    player_name = input("What is your name?: \n")

    select_game_mode = input('Select game mode(normal/hard): \n')
    while select_game_mode not in settings.GAME_MOD:
        select_game_mode = input('Select game mode(normal/hard): \n')

    check_start = input("Type 'start' to begin playing: "
                        "if you want wore commands, please enter: help\n").lower()
    while models.Player.game_commands(check_start) != "start":
        check_start = input("Type 'start' to begin playing: "
                            "if you want wore commands, please enter: help\n").lower()

    if select_game_mode == settings.GAME_MOD[0]:
        player = models.Player(player_name, select_game_mode)
        enemy = models.Enemy(level)
    else:
        player = models.HardPlayer(player_name, select_game_mode)
        enemy = models.HardEnemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)

        except exceptions.EnemyDownExeption:

            if select_game_mode == settings.GAME_MOD[0].lower():
                player.score += 5
                level += 1
                enemy = models.Enemy(level)
                print('lvl up>>>>>>>>>>>\n'
                      'CREATE NEW ENEMY\n'
                      f'Level = {level + 1}')

            if select_game_mode == settings.GAME_MOD[1].lower():
                player.score += 5 * settings.N
                level += 1
                enemy = models.HardEnemy(level)
                print('lvl up>>>>>>>>>>>\n'
                      'CREATE NEW ENEMY\n'
                      f'Level = {level + 1}')


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOverExeption as exc:
        name, score, game_mode = exc.args
        exc.save_score(name, score, game_mode)

        print(f"YOUR SCORE: {score}")
        print("<<<<GameOver>>>>")

    except KeyboardInterrupt:
        pass

    finally:
        print("Good bye!")
