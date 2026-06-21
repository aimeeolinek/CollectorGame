import pygame
from code.Player import Player
from code.Background import Background
from code.EntityFactory import EntityFactory
from code.Score import Score
from code.Const import WIN_WIDTH, WIN_HEIGHT, LEVEL_WIDTH

class Level:
    def __init__(self, window, name, option, player_score):
        self.window = window
        self.name = name
        self.option = option
        self.player_score = player_score
        self.obstacles = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.background = Background()
        self.factory = EntityFactory()
        self.state = "playing"
        self.build_level()
        self.camera_x = 0

    def build_level(self):
        layout = [
        ("collectables", (300, 220)),
        ("obstacles", (500, 240)),
        ("collectables", (700, 220)),
        ("obstacles", (900, 240)),
        ("collectables", (1200, 220)),
        ("obstacles", (1500, 240)),
        ("flags", (1800, 220))
    ]
        for entity_type, pos in layout:
            entity = self.factory.create(entity_type, pos)
            if entity_type == "obstacles":
                self.obstacles.add(entity)
            elif entity_type == "collectables":
                self.collectables.add(entity)
            elif entity_type == "flags":
                self.flags.add(entity)
            self.all_sprites.add(entity)

    def run(self, player_score):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            if self.state == "playing":
                self.all_sprites.update()
                if self.player.rect.centerx > WIN_WIDTH // 2:
                    max_camera = LEVEL_WIDTH - WIN_WIDTH
                    if self.camera_x < max_camera:
                        shift = self.player.rect.centerx - WIN_WIDTH // 2
                        self.player.rect.centerx = WIN_WIDTH // 2
                        self.camera_x += shift
                        for sprite in self.all_sprites:
                            if sprite != self.player:
                                sprite.rect.x -= shift

                # Colisões
                hits = pygame.sprite.spritecollide(self.player, self.collectables, True)
                for _ in hits:
                    player_score[0] += 1

                if pygame.sprite.spritecollideany(self.player, self.obstacles):
                    self.state = "game_over"

                if pygame.sprite.spritecollideany(self.player, self.flags):
                    print("Colidiu com a bandeira")
                    self.show_victory(player_score)
                    return True
                if self.camera_x >= LEVEL_WIDTH - WIN_WIDTH:
                    if self.player.rect.right >= WIN_WIDTH:
                        self.show_victory(player_score)
                        return True

                # Desenho
                self.background.draw(self.window)
                self.all_sprites.draw(self.window)

                font = pygame.font.SysFont("Comic Sans MS", 36)
                score_text = font.render(f"Score: {player_score[0]}", True, (255, 255, 255))
                self.window.blit(score_text, (10, 10))
                pygame.display.flip()

            elif self.state == "game_over":
                self.window.fill((0, 0, 0))
                font = pygame.font.SysFont(
                    "Comic Sans MS", 48)
                msg = font.render("GAME OVER", True, (255, 0, 0))
                self.window.blit(msg, msg.get_rect(
                        center=(WIN_WIDTH//2, WIN_HEIGHT//2)
                    ))

                pygame.display.flip()
                pygame.time.wait(2000)

                return False

    def show_victory(self, player_score):
        self.window.fill((0, 120, 0))

        font_title = pygame.font.SysFont(
            "Comic Sans MS", 48)
        font_score = pygame.font.SysFont(
            "Comic Sans MS", 32)
        title = font_title.render(
            "VOCE VENCEU!", True, (255, 255, 255))

        score = font_score.render(
            f"Flores coletadas: {player_score[0]}",
            True,
            (255, 255, 0))

        self.window.blit(title, title.get_rect(center=(WIN_WIDTH//2, 120)))
        self.window.blit(score, score.get_rect(center=(WIN_WIDTH//2, 190)))
        pygame.display.flip()
        pygame.time.wait(3000)

        