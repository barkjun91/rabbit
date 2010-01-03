# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data/tutorial/image/person/', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    return image


class People(pygame.sprite.Sprite):
    def __init__(self, image1, image2, speed, (x,y)):
	pygame.sprite.Sprite.__init__(self)
	self.type = "person"
	self.image = load_image(image1, -1)
	self.s_image = load_image(image2)
	self.rect = self.s_image.get_rect()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.hp = 1
	self.status = "live"
	
	self.s_x = 0
	self.s_y = 0
    def draw(self, screen, camera):
	self.s_x=self.pos_x-camera.px+self.image.get_width()/2-self.s_image.get_width()/2
	self.s_y=self.pos_y+self.image.get_height()-self.s_image.get_height()/2
	self.rect.x = self.s_x
	self.rect.y = self.s_y

	screen.blit(self.s_image, (self.s_x, self.s_y))
	screen.blit(self.image, (self.pos_x-camera.px, self.pos_y))

    def attacked(self, hitpoint):
	if self.hp > 0:
            self.hp -= hitpoint
	if self.hp <= 0:
	    self.status = "die"
	    print "die"
