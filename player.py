import pygame
from constant import *

class player:

    sprite = pygame.image.load('Textures/player1.png').convert_alpha()
    pos = pygame.math.Vector2(160, 90)
    speed = 60

    def draw(self):
        display.blit(self.sprite, self.pos)
    
    def move_right(self):
        self.pos.x += self.speed * delta

    def move_left(self):
        self.pos.y -= self.speed * delta
    
    def move(self):
        
        if moving_right:
            print("Right")
            self.move_right()
        if moving_left:
            print("Left")
            self.move_left()
    
    def update(self):
        self.move()
