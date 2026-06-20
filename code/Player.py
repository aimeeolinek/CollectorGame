import pygame
from code.Entity import Entity
from code.Const import GRAVITY, JUMP_FORCE, PLAYER_START_X, PLAYER_START_Y, WIN_WIDTH, GROUND_Y

class Player(Entity):
    def __init__(self, pos=(PLAYER_START_X, PLAYER_START_Y)):
        super().__init__("asset/Player_Walk_a.png", pos, (64,72))
        self.velocity_y = 0
        self.speed_x = 5

    def update(self):
        self.handle_input()
        self.apply_gravity()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_Y:
            self.velocity_y = JUMP_FORCE

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIN_WIDTH, self.rect.right)

    def apply_gravity(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity_y = 0