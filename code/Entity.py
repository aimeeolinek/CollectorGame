import pygame
from abc import ABC, abstractmethod

class Entity(pygame.sprite.Sprite, ABC):
    def __init__(self, image_path, pos, size=None):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()

        if size:
            self.image = pygame.transform.scale(
                self.image,
                size
            )

        self.rect = self.image.get_rect(topleft=pos)

    @abstractmethod
    def update(self):
        pass