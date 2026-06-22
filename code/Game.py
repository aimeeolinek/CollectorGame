import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Flower Collector")

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)

            menu_return = menu.run()

            # START GAME
            if menu_return == MENU_OPTION[0]:
                player_score = [0]

                level = Level(self.window, "Level1", menu_return, player_score)
                level_completed = level.run(player_score)

                if level_completed:
                    score.save(menu_return, player_score)

            # SCORE
            elif menu_return == MENU_OPTION[1]:

                score.show()

            # EXIT
            elif menu_return == MENU_OPTION[2]:

                pygame.quit()
                sys.exit()

            else:

                pygame.quit()
                sys.exit()