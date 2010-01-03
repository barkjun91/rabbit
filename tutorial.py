# -*- coding: utf-8 -*-

import main, map, hero, person, arms, mapob
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (640, 480) # screen size set

PEOPLE_LIST = []
OBJECT_LIST = []


def load_person(data):
    people = open('data/tutorial/data/'+data)
    p_count = int(people.readline())
    try:
	for i in range(0, p_count, 1): #c -> for(i = 0; i<1; i ++)
	    name = str(people.readline())
	    if name.startswith("m_farmer"):
	        (x, y) = ( int(people.readline()), int(people.readline()) )
	        PEOPLE_LIST.insert(i, person.People("m_farmer.png", "m_f_shadow.png", 1, (x,y)))
		PEOPLE_LIST[i].hp = 20
    except pygame.error, message:
	print 'Cannot load Person Data'
	raise SystemExit, message

    return p_count

def load_bgobject(data):
    map_ob = open('data/tutorial/data/'+data)
    o_count = int(map_ob.readline())
    try:
	for i in range(0, o_count, 1): #c -> for(i = 0; i<1; i ++)
	    name = str(map_ob.readline())
	    if name.startswith("tree"):
		x, y =  (int(map_ob.readline()),  int(map_ob.readline()))
	        OBJECT_LIST.insert(i, mapob.Mapob("tree",x,y))
    except pygame.error, message:
	print 'Cannot load bgObject Data'
	raise SystemExit, message

    return o_count

def tutorial_main(screen):
    pygame.init()
    viewpos = (0,0)

    player = hero.Player("player", "p_shadow.png",2, (220,320), "test", 5, 0)
    weapon = arms.Weapon("hand")
    maps = map.Map("map.txt", "tiles.png")
    camera = map.Camera(screen)
    p_count = load_person("person.txt")
    o_count = load_bgobject("bgobject.txt")
    draw_list = []

    clash = False
    delay = 1
    clock = pygame.time.Clock()

    person_sprite = pygame.sprite.Group(PEOPLE_LIST[0])
    mapob_sprite = pygame.sprite.Group(OBJECT_LIST[0])
    for i in range(1, p_count, 1):
        person_sprite.add(PEOPLE_LIST[i])
    for i in range(1, o_count, 1):
	mapob_sprite.add(OBJECT_LIST[i])

    draw_list.append(player)
    for i in range(0, p_count, 1):
        if PEOPLE_LIST[i].status.startswith("live"):
            draw_list.append(PEOPLE_LIST[i])
    for i in range(0, o_count, 1):
        draw_list.append(OBJECT_LIST[i])

    while 1:
	screen.fill((255,255,255))
	clock.tick(60)
        player.cmddelay += 1
	player.f_delay += 1
	weapon.f_delay += 1


	for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	    elif event.type == pygame.KEYDOWN:
		hero.press_cmd(event.key, player)
		if event.key == pygame.K_x:
		    player.attack = True
		    weapon.attack = True
		    player.hit(weapon, person_sprite)

	keys = pygame.key.get_pressed()
	
	maps.move(player, camera, keys)

	# -- 일정 시간 키 입력이 없으면 초기화 / 기준 15프레임 
        if player.cmddelay >= 15 or len(player.command) > 10:
	    player.command = ""
	    player.cmddelay = 0

	clash = player.clash(player, person_sprite)
	mapob.pla_clash(player, mapob_sprite, camera)

	maps.draw(screen, viewpos, camera)
	draw_list.sort(key=lambda x: x.s_y)
	for i in range(0, p_count+o_count+1, 1):
	    if draw_list[i].type.startswith("person"):
		if draw_list[i].status.startswith("live"):
		    draw_list[i].draw(screen, camera)
	    elif draw_list[i].type.startswith("player"):
		player.draw(screen, clash, weapon)
		weapon.draw(screen, player, clash)
	    else:
		draw_list[i].draw(screen,camera)

        pygame.display.update()
	pygame.display.flip()
	
 
if __name__ == '__main__':
    main()

