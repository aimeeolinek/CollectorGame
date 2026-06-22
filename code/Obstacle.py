import pygame

from code.Entity import Entity

class Obstacle(Entity):
    def __init__(self, pos):
        super().__init__("asset/Rock_obstacle.png", pos, (40, 28))
        self.rect.inflate_ip(-10, -10)  # Ajusta o retângulo de colisão para ser um pouco menor que a imagem
    def update(self):
        pass  # Obstáculo é estático