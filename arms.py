# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *


class Weapon:
    def __init__(self, weapon):
	self.stand_image = map.load_image(weapon+"_right.png")
	self.stand_image_left = map.load_image(weapon+"_left.png")

	self.weapon = weapon
	att_image = map.load_image(weapon+"_att_right.png")
	self.right_att = hero.get_frame(hero.get_image_list(att_image, 50))
	att_image = map.load_image(weapon+"_att_left.png")
	self.left_att = hero.get_frame(hero.get_image_list(att_image, 50))
 
#	self.rect = self.attack_image.get_rect()

	self.speed = speed(weapon)
	self.dameage = dameage(weapon)
	self.pos_x, self.pos_y = (0, 0)

	self.image_view = self.stand_image
	
	self.f_delay = 0
	self.attack = False
	self.f_attack = 0
    def draw(self, screen, player, clash):
#	if not clash and not player.running and not player.attack:
	if not player.running and not player.attack:
            if player.course.startswith("right"):
                self.image_view = self.stand_image
            elif player.course.startswith("left"):
    	        self.image_view = self.stand_image_left
	if self.attack:
	    if player.course.startswith("right"):
	        if self.f_delay > self.speed:
		    self.f_attack += 1 
	            self.image_view = self.right_att.next()
		    self.f_delay = 0
	    elif player.course.startswith("left"):
	        if self.f_delay > self.speed:
		    self.f_attack += 1 
	            self.image_view = self.left_att.next()
		    self.f_delay = 0
            if self.f_attack == 6:
		print "공격끝!"
		self.attack = False
		self.f_attack = 0
		
	screen.blit(self.image_view, (player.pos_x , player.pos_y))

def speed(name):
    if name.startswith("hand"):
	return 2

def dameage(name):
    if name.startswith("hand"):
	return 10
