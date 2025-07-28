import pygame

SCREEN_SIZE = [320, 180]
WINDOW_SIZE = [SCREEN_SIZE[0] * 4, SCREEN_SIZE[1] * 4]
display = pygame.Surface(SCREEN_SIZE)
screen  = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
delta = clock.tick(60) / 1000.0

moving_right = False
moving_left = False