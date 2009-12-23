# -*- coding: utf-8 -*-

import main
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (800, 600) # screen size set

# define where to get the tile image form in the tiles source image
tile_coords = {
    'a': (0,0), # noraml_ground
    'b': (80,0), # up_ground
    'c': (160,0), # down_ground
    '.': None,
}

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

class Object:
    def __init__(self, image, speed, (x, y)):
	self.image = load_image(image).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
    def draw(self, screen):
	screen.blit(self.image, (self.pos_x, self.pos_y))

class Weapon:
    def __init__(self, weapon):
	self.name = weapon

class Player(Object):
    def __init__(self, image, speed, (x, y), weapon, clothes, rabbits):
	Object.__init__(self, image, speed, (x, y))
	self.weapon = weapon
	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0


def tutorial_main(screen):
    pygame.init()
    player = Player("player.bmp", 2, (0,0), "test", "test", 0)
    while 1:
	screen.fill((255,255,255))
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	player.draw(screen)
        pygame.display.update()
	
 
if __name__ == '__main__':
    main()

