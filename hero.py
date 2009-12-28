# -*- coding: utf-8 -*-

import main, map, arms
import pygame, sys, os, random
from pygame.locals import *

class Player:
    def __init__(self, image, speed, (x, y), weapon, clothes, rabbits):
	self.image = map.load_image(image, 0).convert_alpha()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.damage = arms.weapon(weapon)
	self.clothes = clothes
	self.rabbits = rabbits
	self.spirit = 0
        self.command = ""
        self.cmddelay = 0
	self.running = 0

    def input(self, keys):
	self.pos_x += (keys[K_RIGHT] - keys[K_LEFT]) * self.speed
	self.pos_y += (keys[K_DOWN] - keys[K_UP]) * self.speed * 0.7
	if keys[K_RIGHT]+keys[K_LEFT]+keys[K_DOWN]+keys[K_UP] == 0:
	    self.running = 0

    def draw(self, screen):
	screen.blit(self.image, (self.pos_x, self.pos_y))

    def cmd(self):
	if self.command.startswith("rr"):
	    self.speed = 3
	    self.running = 1
	elif self.command.startswith("ll"):
	    self.speed = 3
	    self.running = 1
	elif self.command.startswith("dd"):
	    self.speed = 2.5
	    self.running = 1
	elif self.command.startswith("uu"):
	    self.speed = 2.5
	    self.running = 1
	else:
	    self.speed = 2

    def attack(self, people):
	print "ㅎㅎ"
	people.hp -= self.damage
	print people.hp
	people.attacked()

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
