#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    COLOR_WHITE
)


class Score:

    best_score = 0

    def __init__(self, window):
        self.window = window

    def save(self, option, player_score):

        if player_score[0] > Score.best_score:
            Score.best_score = player_score[0]

    def show(self):

        self.window.fill((0, 0, 0))

        title_font = pygame.font.SysFont("Comic Sans MS", 42)
        text_font = pygame.font.SysFont("Comic Sans MS", 30)

        title = title_font.render(
            "SCOREBOARD",
            True,
            (255, 255, 255)
        )

        score = text_font.render(
            f"Melhor Score: {Score.best_score}",
            True,
            (255, 255, 0)
        )

        self.window.blit(
            title,
            title.get_rect(center=(WIN_WIDTH//2, 100))
        )

        self.window.blit(
            score,
            score.get_rect(center=(WIN_WIDTH//2, 170))
        )

        pygame.display.flip()

        waiting = True

        while waiting:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    waiting = False