# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *



class People:
    def __init__(self, image1, image2, speed, (x,y)):
	self.image = map.load_image(image1, -1)
	self.s_image = map.load_image(image2)
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.hp = 1
	self.status = "live"

    def draw(self, screen, camera):
	s_x = self.pos_x - camera.px + self.image.get_width()/2 - self.s_image.get_width()/2
	s_y = self.pos_y + self.image.get_height() - self.s_image.get_height()/2
	screen.blit(self.s_image, (s_x, s_y))
	screen.blit(self.image, (self.pos_x-camera.px, self.pos_y))

    def attacked(self):
	if self.hp > 0:
	    print "live"
	elif self.hp <= 0:
	    self.status = "die"
	    print "die"
