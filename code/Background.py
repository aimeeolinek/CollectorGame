import pygame

from code.Const import WIN_WIDTH, PARALLAX_SPEED

class Background:
    """
    Gerencia o fundo do jogo e o efeito de parallax.

    Controla o carregamento, a renderização e o deslocamento
    das camadas de fundo para criar uma sensação de profundidade.
    """
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
        """
        Desenha todas as camadas do fundo na janela,
        aplicando o deslocamento atual de cada uma.
        """
        for layer in self.layers:
            image = self.layers[layer]
            offset = self.offsets[layer]
            # Desenha uma segunda cópia da camada para criar
            # o efeito de rolagem contínua.
            window.blit(image, (offset, 0))
            window.blit(image, (offset + WIN_WIDTH, 0))
    
    def update(self, shift):
        """
        Atualiza o deslocamento das camadas de fundo
        de acordo com o movimento da câmera.
        """
        for layer in self.offsets: 
            self.offsets[layer] -= (shift * PARALLAX_SPEED[layer])
            if self.offsets[layer] <= -WIN_WIDTH: 
                self.offsets[layer] = 0