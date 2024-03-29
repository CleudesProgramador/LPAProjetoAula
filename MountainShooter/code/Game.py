import sys

import pygame as pygame

from code.Level import Level
from code.Menu import Menu
from code.constantesGame import SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, 'Level1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()




