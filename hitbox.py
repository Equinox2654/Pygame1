import pygame, world

class HitBox:

    def __init__(self, pos: pygame.Vector2, size_x: int, size_y: int):
        self.pos = pos
        self.size = [size_x, size_y]
        self.hitbox = pygame.Rect(pos.x, pos.y, size_x, size_y)

    def collide(self, object):
        return self.hitbox.colliderect(object)
