import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.constantesGame import COLOR_WHITE, SCREEN_HEIGHT, MENU_OPTION, EVENT_ENEMY


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)


    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (0 + 10, SCREEN_HEIGHT - 20))
                print(f'fps: {clock.get_fps():.0f}')
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            pygame.display.flip()
        pass

    def level_text(self, text_size, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left=text_position[0], top=text_position[1])
        self.screen.blit(source=text_surface, dest=text_rect)



