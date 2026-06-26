import pygame

from code.Player import Player
from code.Background import Background
from code.EntityFactory import EntityFactory
from code.Const import (COLOR_YELLOW, WIN_WIDTH, WIN_HEIGHT,
                    LEVEL_WIDTH, FPS, COLOR_WHITE, COLOR_RED_2, 
                    COLOR_DARK_GREEN, COLOR_BLACK)
from code.SoundManager import SoundManager

class Level:
    """
    Representa uma fase do jogo.

    Responsável por gerenciar os elementos da fase, a atualização
    dos sprites, a movimentação da câmera, a detecção de colisões
    e os estados de jogo, vitória e derrota.
    """
    def __init__(self, window, name, option, player_score):
        """
        Inicializa o nível com a janela do jogo, o nome do nível,
        a opção selecionada no menu e o score do jogador.
        """
        self.window = window
        self.name = name
        self.option = option
        self.player_score = player_score
        # Inicializa os grupos de sprites para obstáculos, coletáveis e bandeiras
        self.obstacles = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        # Inicializa o jogador e adiciona-o ao grupo de sprites
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.background = Background()
        self.factory = EntityFactory()
        # Define o estado inicial do nível como "playing" e a posição da câmera
        self.state = "playing"
        self.camera_x = 0
        self.sound = SoundManager()
        self.build_level()

    def build_level(self):
        """
        Constrói o layout do nível, criando obstáculos, coletáveis e bandeiras
        com base em posições predefinidas.
        """
        layout = [
        ("collectables", (300, 220)),
        ("obstacles", (500, 240)),
        ("collectables", (700, 220)),
        ("obstacles", (900, 240)),
        ("collectables", (1200, 220)),
        ("obstacles", (1500, 240)),
        ("flags", (1800, 220))
    ]
        # Cria entidades com base no layout definido e as adiciona aos grupos correspondentes
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
        """
        Executa o loop principal do nível, atualizando os elementos,
        detectando colisões e desenhando o fundo e os sprites na janela.
        """
        clock = pygame.time.Clock()
        while True:
            clock.tick(FPS)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return False
            
            if self.state == "playing":
                self.all_sprites.update()

                # Atualiza a posição da câmera com base na posição do jogador
                if self.player.rect.centerx > WIN_WIDTH // 2:
                    max_camera = LEVEL_WIDTH - WIN_WIDTH
                    # Ajusta a posição da câmera para não ultrapassar os limites do nível
                    if self.camera_x < max_camera:
                        shift = self.player.rect.centerx - WIN_WIDTH // 2 
                        self.player.rect.centerx = WIN_WIDTH // 2 
                        self.camera_x += shift 
                        self.background.update(shift) 
                        # Desloca todos os sprites (exceto o jogador) para criar o efeito de movimento da câmera
                        for sprite in self.all_sprites:
                            if sprite != self.player:
                                sprite.rect.x -= shift

                # Detecção de colisões entre o jogador e coletáveis, obstáculos e bandeiras
                hits = pygame.sprite.spritecollide(self.player, self.collectables, True)
                for _ in hits:
                    player_score[0] += 1
                    self.sound.play_collect()
                
                if pygame.sprite.spritecollideany(self.player, self.obstacles):
                    self.state = "game_over"

                if pygame.sprite.spritecollideany(self.player, self.flags):
                    self.show_victory(player_score) 
                    return True
                

                # Desenha o fundo, os sprites e o placar na janela
                self.background.draw(self.window)
                self.all_sprites.draw(self.window)
                
                font = pygame.font.SysFont("Comic Sans MS", 36)
                score_text = font.render(f"Score: {player_score[0]}", True, COLOR_WHITE)
                self.window.blit(score_text, (10, 10))
                pygame.display.flip()

            # Desenha a tela de Game Over, caso seja detectada a colisão com obstáculo.
            elif self.state == "game_over":
                self.window.fill(COLOR_BLACK)
                font = pygame.font.SysFont("Comic Sans MS", 48)
                font_medium = pygame.font.SysFont("Comic Sans MS", 28)
                msg = font.render("GAME OVER", True, COLOR_RED_2)
                msg_2 = font_medium.render("Você colidiu com a pedra!", True, COLOR_WHITE)
                self.window.blit(msg, msg.get_rect(
                        center=(WIN_WIDTH//2, WIN_HEIGHT//2)
                    ))
                self.window.blit(msg_2, msg_2.get_rect(
                        center=(WIN_WIDTH//2, WIN_HEIGHT//2 + 60)
                    ))
                self.sound.stop_music()
                self.sound.play_game_over()
                pygame.display.flip()
                pygame.time.wait(2000)

                return False

    def show_victory(self, player_score):
        """
        Exibe a tela de vitória e a quantidade de flores
        coletadas pelo jogador.
        """
        self.window.fill(COLOR_DARK_GREEN)

        font_title = pygame.font.SysFont("Comic Sans MS", 48)
        font_score = pygame.font.SysFont("Comic Sans MS", 32)

        title = font_title.render("VOCE VENCEU!", True, COLOR_WHITE)
        score = font_score.render(f"Flores coletadas: {player_score[0]}", True, COLOR_YELLOW)
        info = font_score.render("Parabéns!", True, COLOR_WHITE)

        self.window.blit(title, title.get_rect(center=(WIN_WIDTH//2, 120)))
        self.window.blit(score, score.get_rect(center=(WIN_WIDTH//2, 190)))
        self.window.blit(info, info.get_rect(center=(WIN_WIDTH//2, 240)))
        
        self.sound.stop_music()
        self.sound.play_victory()
        pygame.display.flip()
        pygame.time.wait(3000) 

        