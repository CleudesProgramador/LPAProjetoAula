import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.constantesGame import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./asset/menu_bg.png')
        self.rect: Rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 164, 0), ((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.screen.blit(source=text_surface, dest=text_rect)

