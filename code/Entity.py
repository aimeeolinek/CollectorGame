import pygame

from abc import ABC, abstractmethod

class Entity(pygame.sprite.Sprite, ABC):
    """
    Classe abstrata base para as entidades do jogo.

    Fornece os atributos e comportamentos comuns, como imagem,
    posição e área de colisão, além de definir a interface que
    deve ser implementada pelas classes derivadas.
    """
    def __init__(self, image_path, pos, size=None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)

    @abstractmethod
    def update(self):
        """
        Atualiza o estado da entidade.
        Deve ser implementado pelas subclasses.
        """
        pass