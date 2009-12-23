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

def tutorial_main(screen):
    pygame.init()
    while 1:
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
if __name__ == '__main__':
    main()

