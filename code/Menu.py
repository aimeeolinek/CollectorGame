import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_BLACK, WIN_WIDTH, COLOR_RED_1, MENU_OPTION

"""
    Classe que representa o menu do jogo.
    Responsável por exibir a tela inicial do jogo, permitindo que o jogador
    escolha entre iniciar o jogo, consultar score ou sair.
    
"""
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        #pygame.mixer_music.load('./asset/MusicHappy.mp3')
        #pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Flower", COLOR_BLACK, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Collector", COLOR_BLACK, ((WIN_WIDTH / 2), 120))
            self.menu_text(14, "Colete flores e alcance a bandeira! Só cuidado com as pedras!",COLOR_BLACK,((WIN_WIDTH / 2), 160))
            self.menu_text2(12, " press ENTER", COLOR_BLACK, ((WIN_WIDTH / 2), 180))
            self.menu_text2(14,"SETA ESQ/DIR: mover | ESPACO: pular",COLOR_BLACK,((WIN_WIDTH / 2), 295))
            self.menu_text2(12,"Desenvolvido por Aimee Olinek",COLOR_BLACK,((WIN_WIDTH / 2), 315))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_RED_1, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text2(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Console", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)