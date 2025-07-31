import pygame, sys #imports pygame and sys modules
from player import player
from constant import *
import world

pygame.init()
player = player()
colour = (0, 0, 0)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_d:
                player.moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_d:
                player.moving_right = False

            
    
    #Logic Here

    player.update(delta)

    display.fill((146, 244, 255)) #fills screen Blue

    #Visuals Here


    world.draw(display)
    player.draw(display)

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))

    clock.tick(60)
    delta = clock.tick(60) / 1000.0
    pygame.display.flip()
