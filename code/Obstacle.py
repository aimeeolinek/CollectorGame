import pygame

from code.Entity import Entity

class Obstacle(Entity):
    """
    Representa um obstáculo estático do jogo.

    Herda da classe Entity e define a aparência e a área
    de colisão utilizada pelas mecânicas do jogo.
    """
    def __init__(self, pos):
        super().__init__("asset/Rock_obstacle.png", pos, (40, 28))
        self.rect.inflate_ip(-10, -10)  
    def update(self):
        """
        Não realiza atualizações, pois obstáculo é estático.
        """
        pass  