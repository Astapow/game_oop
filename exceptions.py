"""
this module is responsible for self-written errors
"""


class GameOverExeption(Exception):
    """
    if game over raise GameOverExeption
    """

    @staticmethod
    def save_score(name, score, game_mode):
        """
        Save the player's score to the high scores file.
        name: The name of the player
        score: The player's score top 10
        game_mode: The game mode played
        """

        with open('scores.txt', 'a', encoding="utf-8") as file_txt:
            file_txt.write(f"Name: {name} | SCORE: {score} | Game Mode: {game_mode}\n")

        scores = []
        with open('scores.txt', encoding="utf-8") as file_txt:
            for line in file_txt:
                line = line.strip()
                if line:
                    name_, score_, game_mode_ = line.split('|')
                    name_ = name_.strip().split(': ')[1]
                    score_ = int(score_.strip().split(':')[-1])
                    game_mode_ = game_mode_.split(': ')[1]
                    scores.append((name_, score_, game_mode_))

        scores.sort(key=lambda x: x[1], reverse=True)
        scores = scores[:10]

        with open('scores.txt', 'w', encoding="utf-8") as file_txt:
            for name_, score_, game_mode_ in scores:
                file_txt.write(f"Name: {name_} | SCORE: {score_} | Game mode: {game_mode_}\n")


class EnemyDownExeption(Exception):
    """
    raise if enemy_obj has no life
    """
