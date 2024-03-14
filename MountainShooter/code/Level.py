import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass





