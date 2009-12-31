# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *


class Weapon:
    def __init__(self, weapon):
	self.stand_image = map.load_image(weapon+".png")
	stand_left = pygame.transform.flip(self.stand_image, True, False)
	self.stand_image_left = stand_left
	self.weapon = weapon
#	self.attack_image = attackimage 
#	self.rect = self.attack_image.get_rect()
	self.dameage = dameage(weapon)
	self.pos_x, self.pos_y = postion(weapon, "right")

	self.image_view = self.stand_image
	
    def draw(self, screen, player, clash):
	self.pos_x, self.pos_y = postion(self.weapon, player.course)
	if not clash and not player.running:
	    if player.course.startswith("right"):
	        self.image_view = self.stand_image
	    elif player.course.startswith("left"):
		self.image_view = self.stand_image_left
	screen.blit(self.image_view, (self.pos_x+player.pos_x , self.pos_y
                                       +player.pos_y))


def dameage(name):
    if name.startswith("hand"):
	return 10

def postion(name, course):
    if name.startswith("hand"):
	if course.startswith("right"):
	    return (17, 45)
	elif course.startswith("left"):
	    return (7, 45)


