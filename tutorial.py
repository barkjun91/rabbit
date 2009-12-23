# -*- coding: utf-8 -*-

import main
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (800, 600) # screen size set

# define where to get the tile image form in the tiles source image
tile_coords = {
    'a': (0,0), # noraml_ground
    'n': (64,0),
    'b': (128,0),
    '.': None,
}

TILE_SIZE = 64

#load image. where? = main/data/tutorial/~
def load_image(name, colorkey=None):
    fullname = os.path.join('data/tutorial', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

class Map:
    def __init__(self, map, tiles):
	self.tiles = load_image(tiles)
	self.width, self.height = (0, 0)
	l = [line.strip() for line in open('data/tutorial/'+map).readlines()]
	self.map = [[None]*len(l[0]) for j in range(len(l))]

	for i in range(len(l[0])):
	    self.width += TILE_SIZE
	    for j in range(len(l)):
		self.height += TILE_SIZE
		tile = l[j][i]
		tile = tile_coords[tile]
		if tile is None:
		    continue
		elif isinstance(tile, type([])):
		    tile = random.choice(tile)
		cx, cy = tile
	        self.map[j][i] = (cx, cy)

    def draw(self, view, viewpos):
	sx, sy = (self.width, 600)
	bx = viewpos[0]/TILE_SIZE
	by = viewpos[1]/TILE_SIZE
	for x in range(0, sx+TILE_SIZE , TILE_SIZE):
	    i = x/TILE_SIZE  + bx
	    for y in range(0, sy+TILE_SIZE , TILE_SIZE):
		j = y/TILE_SIZE + by
		try:
		    tile = self.map[j][i]
		except IndexError:
		    continue
		if tile is None:
		    continue
		cx, cy = tile
		view.blit(self.tiles, (x, y), (cx, cy, TILE_SIZE, TILE_SIZE))

class Object:
    def __init__(self, image, speed, (x, y)):
	self.image = load_image(image).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
    def draw(self, screen):
	screen.blit(self.image, (self.pos_x, self.pos_y))

class Player(Object):
    def __init__(self, image, speed, (x, y), weapon, clothes, rabbits):
	Object.__init__(self, image, speed, (x, y))
	self.weapon = weapon
	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0

    def input(self, keys):
        self.pos_x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
	self.pos_y += (keys[K_DOWN] - keys[K_UP]) * self.speed

class Weapon:
    def __init__(self, weapon):
	self.name = weapon


def tutorial_main(screen):
    pygame.init()
    viewpos = (0,0)
    player = Player("player.bmp", 2, (0,0), "test", "test", 0)
    map = Map("map.txt", "tiles.png")
    while 1:
	screen.fill((255,255,255))
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	keys = pygame.key.get_pressed()
	
	map.draw(screen, viewpos)
	player.input(keys)
	player.draw(screen)
	
        pygame.display.update()
	
 
if __name__ == '__main__':
    main()

