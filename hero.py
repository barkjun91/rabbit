# -*- coding: utf-8 -*-

import main, map, arms
import pygame, sys, os, random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image1, image2,speed, (x, y), weapon, clothes, rabbits):
	pygame.sprite.Sprite.__init__(self)
	self.image = map.load_image(image1+".png", -1)
	self.c_image = map.load_image(image1+"_clash.png", -1)
	self.s_image = map.load_image(image2, -1)

	player_walk = map.load_image("player_walk.png")
	walk = get_image_list(player_walk, 50)
	self.step = get_frame(walk)
	self.rect = self.s_image.get_rect()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.damage = arms.weapon(weapon)
	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0
        self.command = ""
        self.cmddelay = 0
	self.running = False

	self.delay = pygame.time.Clock()

	self.s_x = 0
	self.s_y = 0

    def input(self, keys):
	self.pos_x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
	self.pos_y += (keys[K_DOWN] - keys[K_UP]) * self.speed * 0.7
	    
    def draw(self, screen, clash):
	self.s_x=self.pos_x+self.s_image.get_width()/4
	self.s_y=self.pos_y+self.image.get_height()-self.s_image.get_height()/2
	self.rect.x = self.s_x
	self.rect.y = self.s_y
	screen.blit(self.s_image, (self.s_x, self.s_y)) 
	if not clash and not self.running:
	    screen.blit(self.image, (self.pos_x, self.pos_y))
	elif clash:
	    screen.blit(self.c_image, (self.pos_x, self.pos_y))
	elif self.running:
	    rect = Rect((self.pos_x, self.pos_y, 75, 50))
	    screen.blit(self.step.next(), rect)	
	    

    def cmd(self):
	if self.command.startswith("rr"):
	    self.speed = 3
	    self.running = True
	elif self.command.startswith("ll"):
	    self.speed = 3
	    self.running = True
	elif self.command.startswith("dd"):
	    self.speed = 2.5
	    self.running = True
	elif self.command.startswith("uu"):
	    self.speed = 2.5
	    self.running = True
	else:
	    self.speed = 2
	    self.running = False


    def attack(self, people, clash):
	if clash:
	    people[1].hp -= self.damage
	print people[1].hp
	people[1].attacked()

    def clash(self, sprite, group):
	if pygame.sprite.spritecollideany(sprite, group):
	    return True
	return False

def press_cmd(keys, player):
    if keys == pygame.K_RIGHT:
	player.command = player.command + 'r'
	player.cmddelay = 0
    if keys == pygame.K_UP:
	player.command = player.command + 'u'
	player.cmddelay = 0
    if keys == pygame.K_DOWN:
	player.command = player.command + 'd'
	player.cmddelay = 0
    if keys == pygame.K_LEFT:
	player.command = player.command + 'l'
	player.cmddelay = 0
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


