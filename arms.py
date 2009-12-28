# -*- coding: utf-8 -*-

import main, map, hero, people
import pygame, sys, os, random
from pygame.locals import *


def weapon(name):
    if name.startswith("hand"):
	return 10
