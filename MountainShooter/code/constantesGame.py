# Cor do texto (Nome do game)
import pygame

COLOR_ORANGE = (255, 164, 0)
# Cor do texto (Nome da opção de menu)
COLOR_WHITE = (255, 255, 255)
# Cor do texto ao ser selecionado pela seta
COLOR_YELLOW = (255, 255, 100)

# Opção de menu
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "EXIT")
# Valor fixo da largura e altura da tela(screen)
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 324
# Criar o movimento para cada entidade do background - Movimento da imagens da figura
ENTITY_SPEED = {'level1bg0': 0,
                'level1bg1': 1,
                'level1bg2': 2,
                'level1bg3': 3,
                'level1bg4': 4,
                'level1bg5': 5,
                'level1bg6': 6,
                'player1': 3,
                'player1Shot': 2,
                'player2': 3,
                'player2Shot': 2,
                'enemy1': 1,
                'enemy1Shot': 5,
                'enemy2': 1,
                'enemy2Shot': 3,
                }

# Criar as vidas das Entidades do jogo.
ENTITY_HEALTH = {'level1bg0': 999,
                 'level1bg1': 999,
                 'level1bg2': 999,
                 'level1bg3': 999,
                 'level1bg4': 999,
                 'level1bg5': 999,
                 'level1bg6': 999,
                 'player1': 300,
                 'player1Shot': 1,
                 'player2': 300,
                 'player2Shot': 1,
                 'enemy1': 200,
                 'enemy1Shot': 1,
                 'enemy2': 200,
                 'enemy2Shot': 1,
                 }

ENTITY_SHOT_DELAY = {'player1': 10,
                     'player2': 5,
                     'enemy1': 80,
                     'enemy2': 160,
                     }

# Criar os movimentos do player1 e player2
PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                   'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'player1': pygame.K_l,
                    'player2': pygame.K_LCTRL,
                    }

EVENT_ENEMY = pygame.USEREVENT + 1
