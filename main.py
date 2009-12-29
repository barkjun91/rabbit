#-*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import tutorial


#stage = ["title", "main", "tutorial","stage1"]
stage = 3


def main():
    SCREEN_SIZE = (640, 480) # screen size set
    # Start up pygame/make screen
    pygame.init() 

    #screen seting
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    #title set
    pygame.display.set_caption('Rabbit Hazard') 
    game_status = True
    clock = pygame.time.Clock()
    #call stage1.main
    while game_status:
	clock.tick(60)
    	if stage == 3:
           game_status = tutorial.tutorial_main(screen)


if __name__ == '__main__':
    main()
 

