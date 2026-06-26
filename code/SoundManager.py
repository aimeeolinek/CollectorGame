import pygame


class SoundManager:
    """
    Gerencia as músicas e efeitos sonoros do jogo.

    Responsável por carregar, reproduzir e interromper músicas
    de fundo e efeitos sonoros utilizados durante a execução.
    """
    def __init__(self):
        pygame.mixer.init()

        # Músicas
        self.menu_music = "asset/MusicHappy2.mp3"
        self.level_music = "asset/MusicHappy2.mp3"

        # Efeitos sonoros
        self.collect_sound = pygame.mixer.Sound(
            "asset/CollectSound.wav"
        )
        self.game_over_sound = pygame.mixer.Sound(
            "asset/GameOverSound.wav"
        )
        self.victory_sound = pygame.mixer.Sound(
            "asset/VictorySound.wav"
        )

        # Volume dos efeitos
        self.collect_sound.set_volume(0.7)
        self.game_over_sound.set_volume(0.7)
        self.victory_sound.set_volume(0.7)

    # Músicas
    def play_menu_music(self):
        """
        Reproduz a música do menu em loop.
        """
        pygame.mixer.music.load(self.menu_music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def play_level_music(self):
        """
        Reproduz a música da fase em loop.
        """
        pygame.mixer.music.load(self.level_music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """
        Interrompe a música atual.
        """
        pygame.mixer.music.stop()

   
    # Efeitos
    def play_collect(self):
        """
        Reproduz o efeito de coleta.
        """
        self.collect_sound.play()

    def play_game_over(self):
        """
        Reproduz o efeito de derrota.
        """
        self.game_over_sound.play()

    def play_victory(self):
        """
        Reproduz o efeito de vitória.
        """
        self.victory_sound.play()