import pygame

from abc import ABC, abstractmethod
"""
    Classe abstrata que representa uma entidade no jogo.
    Herda de pygame.sprite.Sprite e define a interface para todas as entidades do jogo,
    incluindo a exibição da imagem, a posição e o tamanho.
"""
class Entity(pygame.sprite.Sprite, ABC):
    def __init__(self, image_path, pos, size=None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)

    @abstractmethod
    def update(self):
        pass