import pygame
from constant import *
from hitbox import HitBox
from world import move as move_rect
from world import tile_rects

class player:

    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.sprite = pygame.image.load('Textures/player1.png').convert_alpha()
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 180
        self.gravity_force = gravity
        self.hitbox = HitBox(pygame.math.Vector2(160, 90), self.sprite.get_width(), self.sprite.get_height())
        self.y_direction = 0

    def draw(self, display: pygame.Surface):
        display.blit(self.sprite, self.hitbox.pos)
    
    def move_right(self, delta):
        self.velocity.x += self.speed * delta

    def move_left(self, delta):
        self.velocity.x -= self.speed * delta / 2

    def move(self, delta):
        if self.moving_right:
            self.move_right(delta)
        if self.moving_left:
            self.move_left(delta)
        self.apply_gravity(delta)

    
    def apply_gravity(self, delta):
        self.y_direction += self.gravity_force * delta
        if self.y_direction > 15:
            self.y_direction = 15
        self.velocity.y += self.y_direction
        

    def update(self, delta):
        self.move(delta)
        self.hitbox.hitbox, collisions = move_rect(self.hitbox.hitbox, self.velocity, tile_rects)
        self.hitbox.pos = pygame.math.Vector2(self.hitbox.hitbox.x, self.hitbox.hitbox.y)
        self.velocity = pygame.math.Vector2(0, 0)
