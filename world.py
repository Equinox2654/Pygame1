import pygame
from constant import *

pygame.init()

grass_sprite = pygame.image.load('Textures/Grass.png').convert_alpha()
dirt_sprite = pygame.image.load('Textures/Dirt.png').convert_alpha()
tile_rects = []

game_map = [
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['2','2','2','2','2','1','1','1','0','0','0','0','0','1','1','1','1','1','1','1'],
    ['2','2','2','2','2','2','2','2','1','1','1','1','1','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
    ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
]

def draw(display):
    y = 0
    for row in game_map:
        x = 0
        for cell in row:
            if cell == '1':
                display.blit(grass_sprite, (x * TILE_SIZE, y * TILE_SIZE))
            elif cell == '2':
                display.blit(dirt_sprite, (x * TILE_SIZE, y *TILE_SIZE))
            if cell != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'Top': False, 'Bottom': False, 'Right': False, 'Left': False}
    rect.x += movement.x
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement.x > 0:
            rect.right = tile.left
            collision_types['Right'] = True
        elif movement.x < 0:
            rect.left = tile.right
            collision_types['Left'] = True
    rect.y += movement.y
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement.y > 0:
            rect.bottom = tile.top
            collision_types["Bottom"] = True
        elif movement.y < 0:
            rect.top = tile.bottom
            collision_types['Top'] = True

    return rect, collision_types
