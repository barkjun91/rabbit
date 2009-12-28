# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *



class Person:
    def __init__(self, image, speed, (x,y)):
	self.image = map.load_image(image, -1).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.hp = 1
	self.status = "live"

    def draw(self, screen, camera):
	screen.blit(self.image, (self.pos_x-camera.px, self.pos_y))

    def attacked(self):
	if self.hp > 0:
	    print "live"
	elif self.hp <= 0:
	    self.status = "die"
	    print "die"
