# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (800, 600) # screen size set

PERSON_LIST = []

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

def load_person(data):
    person = open('data/tutorial/'+data)
    p_count = int(person.readline())
    try:
	for i in range(0, p_count, 1): #c -> for(i = 0; i<1; i ++)
	    print person.readline()
	    x = person.readline()
	    y = person.readline()
	    hp = person.readline()
	    PERSON_LIST.insert(i, Person("m_farmer.bmp", 2, (x,y),hp))
    except pygame.error, message:
	print 'Cannot load Person Data'
	raise SystemExit, message

    return p_count


class Object:
    def __init__(self, image, speed, (x, y)):
	self.image = load_image(image).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
    def draw(self, screen):
	screen.blit(self.image, (self.pos_x, self.pos_y))

class Person(Object):
    def __init__(self, image, speed, (x,y), hp):
	Object.__init__(self, image, speed, (x,y))
	self.hp = hp

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
    player = Player("player.bmp", 2, (220,490), "test", "test", 0)
    maps = map.Map("map.txt", "tiles.png")
    camera = map.Camera(screen)
    count = load_person("person.txt")

    print PERSON_LIST[0].hp

    while 1:
	screen.fill((255,255,255))
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	keys = pygame.key.get_pressed()
	
	maps.move(player, camera, keys)

	maps.draw(screen, viewpos, camera)
	player.draw(screen)
        pygame.display.update()
	
 
if __name__ == '__main__':
    main()

