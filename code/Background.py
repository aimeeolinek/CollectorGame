import pygame

from code.Const import WIN_WIDTH, PARALLAX_SPEED

class Background:
    def __init__(self):
        # Carrega cada layer
        self.layers = {
            'Level1Bg0': pygame.image.load("asset/Level1Bg0.png").convert(),
            'Level1Bg1': pygame.image.load("asset/Level1Bg1.png").convert_alpha(),
            'Level1Bg2': pygame.image.load("asset/Level1Bg2.png").convert_alpha(),
            'Level1Bg3': pygame.image.load("asset/Level1Bg3.png").convert_alpha(),
        }
        self.offsets = {
            layer: 0
            for layer in self.layers}
        
    def draw(self, window):
        for layer in self.layers:
            image = self.layers[layer]
            offset = self.offsets[layer]
            window.blit(image, (offset, 0))
            window.blit(image, (offset + WIN_WIDTH, 0))
    
    def update(self, shift):
        for layer in self.offsets: 
            self.offsets[layer] -= (shift * PARALLAX_SPEED[layer])
            if self.offsets[layer] <= -WIN_WIDTH: 
                self.offsets[layer] = 0