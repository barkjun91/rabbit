# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data/tutorial/image/arms/', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    return image


class Weapon(pygame.sprite.Sprite):
    def __init__(self, weapon):
	pygame.sprite.Sprite.__init__(self)
	self.stand_image = load_image(weapon+"_right.png")
	self.stand_image_left = load_image(weapon+"_left.png")

	self.weapon = weapon
	att_image = load_image(weapon+"_att_right.png")
	self.right_att = hero.get_frame(hero.get_image_list(att_image, 50))
	att_image = load_image(weapon+"_att_left.png")
	self.left_att = hero.get_frame(hero.get_image_list(att_image, 50))
 
	self.att_area_image = load_image(weapon+"_att_area.png", -1)
	self.rect = self.att_area_image.get_rect()

	self.speed = speed(weapon)
	self.damage = damage(weapon)
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
		self.attack = False
		self.f_attack = 0
        if player.course.startswith("right"):
            s_x = player.s_x+player.s_image.get_width()/2
        elif player.course.startswith("left"):
    	    s_x = player.s_x-player.s_image.get_width()/2
	x, y = (self.att_area_image.get_width(),
                self.att_area_image.get_height())

	self.rect = Rect((s_x, player.s_y, x, y)) 
	screen.blit(self.att_area_image, (s_x, player.s_y))	
	screen.blit(self.image_view, (player.pos_x , player.pos_y))

def speed(name):
    if name.startswith("hand"):
	return 2

def damage(name):
    if name.startswith("hand"):
	return 5
