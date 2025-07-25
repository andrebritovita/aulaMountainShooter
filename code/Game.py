#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.mixer
from pygame import event

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()  # Recebe uma String

            # Se menu_option for qualquer uma das Strings das posições 0, 1 ou 2
            # a condição será True e o bloco de código será executado
            if menu_return in ([MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]):
                plyer_score = [0, 0]  # [Player1, Player1]
                level = Level(self.window, 'Level1', menu_return, plyer_score)
                level_return = level.run(plyer_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, plyer_score)
                    level_return = level.run(plyer_score)
                    if level_return:
                        score.save(menu_return, plyer_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # End pygame
            else:
                pass
