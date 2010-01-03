# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *


class Mapob(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
	pygame.sprite.Sprite.__init__(self)
	self.object = map.load_image(name+".png")
	self.pos_x = x
	self.pos_y = y
	self.area = map.load_image("area_"+name+".png")
	self.s_x, self.s_y = shadow(name, self.pos_x, self.pos_y)
	self.rect = Rect((self.s_x, self.s_y, 
                          self.area.get_width(), self.area.get_height()))
	self.type = "mapobject"

    def draw(self, screen, camera):
	self.rect = Rect((self.s_x-camera.px, self.s_y, 
                          self.area.get_width(), self.area.get_height()))
	screen.blit(self.area, (self.s_x-camera.px, self.s_y))
	screen.blit(self.object, (self.pos_x-camera.px, self.pos_y))


#    def per_clash

def shadow(n, x, y):
    if n.startswith("tree"):
	return (x+49, y+274)
    return (0,0)

def pla_clash(sprite, group, camera):
    who = pygame.sprite.spritecollideany(sprite, group)
    if who:
        if sprite.pos.startswith("up"): 
	    sprite.pos_y += sprite.speed * 0.7
        elif sprite.pos.startswith("down"): 
	    sprite.pos_y -= sprite.speed * 0.7
	elif camera.px <= 0:
	    if sprite.pos.startswith("right"):
	        sprite.pos_x -= sprite.speed 
            elif sprite.pos.startswith("left"): 
	        sprite.pos_x += sprite.speed 
        elif camera.px > 0:
	    if sprite.pos.startswith("right"):
	        camera.px -= sprite.speed 
            elif sprite.pos.startswith("left"): 
		camera.px += sprite.speed 
