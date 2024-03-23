import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.constantesGame import SCREEN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./asset/menu_bg.png')
        self.rect: Rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        menu_option = 0
        while True:
            # Desenhar na tela
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, (SCREEN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, (SCREEN_WIDTH / 2, 125))
            # Criar um For para percorrer o texto do Menu (ao ser clicado mudar a cor
            for i in range(len(MENU_OPTION)):
                if (i == menu_option):
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (SCREEN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (SCREEN_WIDTH / 2, 200 + 30 * i))
            pygame.display.flip()
            # Criar um evento para fechar a tela do jogo e encerrar o programa
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Percorrer com um For o texto do Menu mudando a cor pressionando a tecla
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.screen.blit(source=text_surface, dest=text_rect)
