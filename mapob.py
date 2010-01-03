# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *


class Mapob:
    def __init__(self, name, x, y):
	self.object = map.load_image(name+".png")
	self.pos_x = x
	self.pos_y = y
	self.area = map.load_image("area_"+name+".png")
	self.s_x, self.s_y = shadow(name, self.pos_x, self.pos_y)
	self.rect = self.area.get_rect()
	self.type = "mapobject"

    def draw(self, screen, camera):
	screen.blit(self.area, (self.s_x-camera.px, self.s_y))
	screen.blit(self.object, (self.pos_x-camera.px, self.pos_y))

def shadow(n, x, y):
    if n.startswith("tree"):
	return (x+49, y+274)
    return (0,0)
