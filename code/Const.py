import pygame 

# Configurações da Janela 
WIN_WIDTH = 576 
WIN_HEIGHT = 324 
FPS = 60 

GROUND_Y = WIN_HEIGHT - 50

# Cores (Fallbacks caso falte alguma imagem)
COLOR_BG = (135, 206, 235)  # Azul céu 
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0) 
COLOR_GREEN = (34, 139, 34) 
COLOR_RED = (220, 20, 60) 
COLOR_YELLOW = (255, 215, 0)
COLOR_ORANGE = (255, 165, 0)

# Opções do Menu
MENU_OPTION = ("Start Game",
               "Score", 
               "Exit")

# Eventos Personalizados             
TIMEOUT_STEP = 1000  # Tempo em milissegundos para cada passo do timeout
TIMEOUT_LEVEL = 30000  # Tempo total em milissegundos para o timeout do nível
# Física do Jogo 


GRAVITY = 1
JUMP_FORCE = -18

PLAYER_START_X = 50
PLAYER_START_Y = GROUND_Y - 72  # Altura do player (72) para ficar em cima do chão

# Regras do Jogo 
SCORE_TO_WIN = 10  # Número X de frutas para vencer 
SPAWN_DELAY = 1500  # Tempo em milissegundos para novos spawns