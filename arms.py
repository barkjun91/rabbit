# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *


class Weapon:
    def __init__(self, weapon):
	self.stand_image = map.load_image(weapon+".png")
#	self.attack_image = attackimage 
#	self.rect = self.attack_image.get_rect()
	self.dameage = dameage(weapon)
	self.pos_x, self.pos_y = postion(weapon)
    def draw(self, screen, player):
	screen.blit(self.stand_image, (self.pos_x+player.pos_x , self.pos_y
                                       +player.pos_y))


def dameage(name):
    if name.startswith("hand"):
	return 10

def postion(name):
    if name.startswith("hand"):
	return (17, 45)
