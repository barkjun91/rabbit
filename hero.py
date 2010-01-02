# -*- coding: utf-8 -*-

import main, map, arms
import pygame, sys, os, random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image1, image2,speed, (x, y), clothes, rabbits):
	pygame.sprite.Sprite.__init__(self)
	self.type = "player"

	self.image = map.load_image(image1+"_right.png", -1)
	self.image_left = map.load_image(image1+"_left.png",-1)

	self.c_image = map.load_image(image1+"_clash_right.png", -1)
	self.c_image_left = map.load_image(image1+"_clash_left.png", -1)

	self.s_image = map.load_image(image2, -1)

	player_run = map.load_image("player_run_right.png")
	self.right_run = get_frame(get_image_list(player_run, 50))
	player_run = map.load_image("player_run_left.png")
	self.left_run = get_frame(get_image_list(player_run, 50))	

	player_att = map.load_image("player_att_right.png")
	self.right_att = get_frame(get_image_list(player_att, 50))
	player_att = map.load_image("player_att_left.png")
	self.left_att = get_frame(get_image_list(player_att, 50))

	self.image_view = self.image

	self.rect = self.s_image.get_rect()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)

	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0
        self.command = ""
        self.cmddelay = 0

	self.running = False
	self.attack = False	
	self.f_attack = 0

	self.s_x = 0
	self.s_y = 0
	self.f_delay = 0
	self.course = "right"

    def input(self, keys):
	self.pos_x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
	self.pos_y += (keys[K_DOWN] - keys[K_UP]) * self.speed * 0.7
	    
    def draw(self, screen, clash, weapon):
	rect = Rect((self.pos_x, self.pos_y, 75, 50))
	self.s_x=self.pos_x+self.s_image.get_width()/4
	self.s_y=self.pos_y+self.image.get_height()-self.s_image.get_height()/2
	self.rect.x = self.s_x
	self.rect.y = self.s_y
	if not clash and not self.running and not self.attack:
	    if self.course.startswith("right"):
	        self.image_view = self.image
	    elif self.course.startswith("left"):
		self.image_view = self.image_left

	elif self.attack:
	    if self.course.startswith("right"):
	        if self.f_delay > weapon.speed:
		    self.f_attack += 1 
	            self.image_view = self.right_att.next()
		    self.f_delay = 0
	    elif self.course.startswith("left"):
	        if self.f_delay > weapon.speed:
		    self.f_attack += 1 
	            self.image_view = self.left_att.next()
		    self.f_delay = 0
	    if self.f_attack == 6:
		print "finish attack of rabbit!"
		self.attack = False
		self.f_attack = 0

	elif clash:
	    if self.course.startswith("right"):
	        self.image_view = self.c_image 
	    elif self.course.startswith("left"):
		self.image_view = self.c_image_left

	elif self.running:
	    if self.course.startswith("right"):
	        if self.f_delay > 15:
	            self.image_view = self.right_run.next()
		    self.f_delay = 0
	    elif self.course.startswith("left"):
	        if self.f_delay > 15:
	            self.image_view = self.left_run.next()
		    self.f_delay = 0
	screen.blit(self.s_image, (self.s_x, self.s_y))  
	screen.blit(self.image_view, rect)
	

    def cmd(self):
	if self.command.endswith("rr"): #and not self.command.endswith("rrr"):
	    self.speed = 3
	    self.running = True
	elif self.command.endswith("ll"): #and not self.command.endswith("lll"):
	    self.speed = 3
	    self.running = True
	elif self.command.endswith("dd"): #and not self.command.endswith("ddd"):
	    self.speed = 2.5
	    self.running = True
	elif self.command.endswith("uu"): #and not self.command.endswith("uuu"):
	    self.speed = 2.5
	    self.running = True
	else:
	    self.speed = 2
	    self.running = False


    def hit(self, wea, peo):
        who = pygame.sprite.spritecollideany(wea, peo)
	if who and who.status.startswith("live"):
	    print "yap yap!"
	    who.attacked(wea.damage)
	else:
	    print "vain effort!"

    def clash(self, pla, peo):
        who = pygame.sprite.spritecollideany(pla, peo)
	if who and who.status.startswith("live"):
	    return True
	return False

def press_cmd(keys, player):
    if keys == pygame.K_RIGHT:
	player.command = player.command + 'r'
	player.cmddelay = 0
	player.course = "right"
    if keys == pygame.K_UP:
	player.command = player.command + 'u'
	player.cmddelay = 0
    if keys == pygame.K_DOWN:
	player.command = player.command + 'd'
	player.cmddelay = 0
    if keys == pygame.K_LEFT:
	player.command = player.command + 'l'
	player.cmddelay = 0
	player.course = "left"
    player.cmd()
    print player.command
    print player.pos_x
    print player.pos_y

def get_image_list(image, frame_width):
    image_list = []
    height = image.get_height()
    for frame in xrange(image.get_width()/frame_width):
        image_list.append(image.subsurface(Rect(frame*frame_width, 0,
                                           frame_width, height)))
    return image_list

def get_frame(frame_list):
    while True:
        for frame in frame_list:
            yield frame


