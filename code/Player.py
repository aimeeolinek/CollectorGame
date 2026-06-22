import pygame

from code.Entity import Entity
from code.Const import GRAVITY, JUMP_FORCE, PLAYER_START_X, PLAYER_START_Y, WIN_WIDTH, GROUND_Y

class Player(Entity):
    def __init__(self, pos=(PLAYER_START_X, PLAYER_START_Y)):
        super().__init__("asset/Player_Walk_a.png", pos, (64,72))
        self.frames = [
            pygame.transform.scale(
                pygame.image.load("asset/Player_Walk_a.png").convert_alpha(),(64, 72)),
            pygame.transform.scale(
                pygame.image.load("asset/Player_Walk_b.png").convert_alpha(),(64, 72))]
        self.image = self.frames[0]
        self.velocity_y = 0
        self.speed_x = 5
        self.current_frame = 0
        self.animation_timer = 0

    def update(self):
        self.handle_input()
        self.apply_gravity()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
            moving = True
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
            moving = True
        if moving:
            self.animate()
        else:
            self.current_frame = 0 
            self.image = self.frames[0]  # Reset to the first frame when not moving

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

    def animate(self):
        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.animation_timer = 0