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
	    name = str(person.readline())
	    if name.startswith("m_farmer"):
	        x = int(person.readline())
	        y = int(person.readline())
	        PERSON_LIST.insert(i, Person("m_farmer.bmp", 2, (x,y)))
		PERSON_LIST[i].hp = 100
    except pygame.error, message:
	print 'Cannot load Person Data'
	raise SystemExit, message

    return p_count

def press_cmd(keys, player):
    if keys == pygame.K_RIGHT:
	player.command = player.command + 'r'
	player.cmddelay = 0
    if keys == pygame.K_UP:
	player.command = player.command + 'u'
	player.cmddelay = 0
    if keys == pygame.K_DOWN:
	player.command = player.command + 'd'
	player.cmddelay = 0
    if keys == pygame.K_LEFT:
	player.command = player.command + 'l'
	player.cmddelay = 0
    player.cmd()
    print player.command
    
class Object:
    def __init__(self, image, speed, (x, y)):
	self.image = load_image(image).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)

class Person(Object):
    def __init__(self, image, speed, (x,y)):
	Object.__init__(self, image, speed, (x,y))
	self.hp = 1
    def draw(self, screen, camera):
	screen.blit(self.image, (self.pos_x-camera.px, self.pos_y))

class Player(Object):
    def __init__(self, image, speed, (x, y), weapon, clothes, rabbits):
	Object.__init__(self, image, speed, (x, y))
	self.weapon = weapon
	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0
        self.command = ""
        self.cmddelay = 0
	self.running = 0

    def input(self, keys):
	self.pos_x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
	self.pos_y += (keys[K_DOWN] - keys[K_UP]) * self.speed * 0.7
	if keys[K_RIGHT]+keys[K_LEFT]+keys[K_DOWN]+keys[K_UP] == 0:
	    self.running = 0

    def draw(self, screen):
	screen.blit(self.image, (self.pos_x, self.pos_y))

    def cmd(self):
	if self.command.startswith("rr"):
	    self.speed = 4
	    self.running = 1
	elif self.command.startswith("ll"):
	    self.speed = 4
	    self.running = 1
	elif self.command.startswith("dd"):
	    self.speed = 3
	    self.running = 1
	elif self.command.startswith("uu"):
	    self.speed = 3
	    self.running = 1
	else:
	    self.speed = 2




class Weapon:
    def __init__(self, weapon):
	self.name = weapon

def tutorial_main(screen):
    pygame.init()
    viewpos = (0,0)
    player = Player("player.bmp", 2, (220,490), "test", "test", 0)
    maps = map.Map("map.txt", "tiles.png")
    camera = map.Camera(screen)
    p_count = load_person("person.txt")

    while 1:
	screen.fill((255,255,255))
        player.cmddelay += 1
	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	    elif event.type == pygame.KEYDOWN:
		press_cmd(event.key, player)

	keys = pygame.key.get_pressed()
	maps.move(player, camera, keys)

	# -- 일정 시간 키 입력이 없으면 초기화 / 기준 15프레임 
        if player.cmddelay >= 15:
	    player.command = ""
	    player.cmddelay = 0


	maps.draw(screen, viewpos, camera)
	for i in range(0, p_count, 1):
	    PERSON_LIST[i].draw(screen, camera)
	player.draw(screen)
        pygame.display.update()
	
 
if __name__ == '__main__':
    main()

