import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Background:
    def __init__(self):
        # Carrega cada layer
        self.layers = {
            'Level1Bg0': pygame.image.load("asset/Level1Bg0.png").convert(),
            'Level1Bg1': pygame.image.load("asset/Level1Bg1.png").convert_alpha(),
            'Level1Bg2': pygame.image.load("asset/Level1Bg2.png").convert_alpha(),
            'Level1Bg3': pygame.image.load("asset/Level1Bg3.png").convert_alpha(),
        }
        
    def draw(self, window):
        for layer in self.layers:
            window.blit(self.layers[layer], (0,0))