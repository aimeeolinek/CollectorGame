"""
    Constantes do jogo.
    Contém configurações da janela, dimensões do cenário, 
    parâmetros do jogador, física do jogo, opções do menu e cores.
    
"""

# Configurações da Janela 
WIN_WIDTH = 576 
WIN_HEIGHT = 324 
FPS = 60 

# Cenário
GROUND_Y = WIN_HEIGHT - 50
LEVEL_WIDTH = 2000

# Player
PLAYER_START_X = 50
PLAYER_START_Y = GROUND_Y - 72  # Altura do player (72) para ficar em cima do chão

# Física
GRAVITY = 1
JUMP_FORCE = -18

# Opções do Menu
MENU_OPTION = ("Start Game",
               "Score", 
               "Exit")

# Cores
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0) 
COLOR_RED_1 = (220, 20, 60)
COLOR_RED_2 = (255, 0, 0) 
COLOR_YELLOW = (255, 215, 0)
DARK_GREEN = (0, 120, 0)

# Parallax
PARALLAX_SPEED = {
    'Level1Bg0': 0.0,
    'Level1Bg1': 0.3,
    'Level1Bg2': 0.5,
    'Level1Bg3': 0.8,
}






