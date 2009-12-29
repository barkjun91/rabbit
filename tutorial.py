# -*- coding: utf-8 -*-

import main, map, hero, person
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (640, 480) # screen size set

PEOPLE_LIST = []

def load_person(data):
    people = open('data/tutorial/'+data)
    p_count = int(people.readline())
    try:
	for i in range(0, p_count, 1): #c -> for(i = 0; i<1; i ++)
	    name = str(people.readline())
	    if name.startswith("m_farmer"):
	        (x, y) = ( int(people.readline()), int(people.readline()) )
	        PEOPLE_LIST.insert(i, person.People("m_farmer.png", 1, (x,y)))
		PEOPLE_LIST[i].hp = 100
    except pygame.error, message:
	print 'Cannot load Person Data'
	raise SystemExit, message

    return p_count

def tutorial_main(screen):
    pygame.init()
    viewpos = (0,0)
    player = hero.Player("player.png", 2, (220,320), "hand", "test", 5)
    maps = map.Map("map.txt", "tiles.png")
    camera = map.Camera(screen)
    p_count = load_person("person.txt")

    while 1:
	screen.fill((255,255,255))
        player.cmddelay += 1

	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	    elif event.type == pygame.KEYDOWN:
		hero.press_cmd(event.key, player)
		if event.key == pygame.K_x:
		    player.attack(PERSON_LIST[0])

	keys = pygame.key.get_pressed()
	maps.move(player, camera, keys)

	# -- 일정 시간 키 입력이 없으면 초기화 / 기준 15프레임 
        if player.cmddelay >= 15:
	    player.command = ""
	    player.cmddelay = 0


	maps.draw(screen, viewpos, camera)
	for i in range(0, p_count, 1):
	    if PEOPLE_LIST[i].status.startswith("live"):
	        PEOPLE_LIST[i].draw(screen, camera)	
	player.draw(screen)
        pygame.display.update()
	
 
if __name__ == '__main__':
    main()

