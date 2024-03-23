import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.constantesGame import SCREEN_WIDTH, SCREEN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (SCREEN_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('player1', (10, SCREEN_HEIGHT / 2 - 40))
            case 'player2':
                return Player('player2', (10, SCREEN_HEIGHT / 2 + 40))
            case 'enemy1':
                return Enemy('enemy1', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))
            case 'enemy2':
                return Enemy('enemy2', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))
