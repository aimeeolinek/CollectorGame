import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    """
    Classe que representa o jogo.
    Responsável por gerenciar o fluxo principal do jogo, incluindo a inicialização,
    a execução do menu, a transição entre níveis e a exibição do placar.
    """
    def __init__(self):
        # Inicializa o pygame e desenha a janela do jogo.
        pygame.init() 
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Flower Collector")

    def run(self):
        """
        Executa o loop principal do jogo.

        Gerencia a navegação entre os estados do sistema, exibindo o menu,
        iniciando uma partida, mostrando o placar ou encerrando a aplicação
        de acordo com a opção escolhida pelo jogador.
        """
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