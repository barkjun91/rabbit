# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *


class Weapon:
    def __init__(self, weapon):
	self.stand_image = "test"
	self.dameage = dameage(weapon)


def dameage(name):
    if name.startswith("hand"):
	return 10
