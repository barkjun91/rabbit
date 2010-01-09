# -*- coding: utf-8 -*-

import main, map
import pygame, sys, os, random
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data/tutorial/image/person/', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    return image


class People(pygame.sprite.Sprite):
    def __init__(self, image1, image2, speed, (x,y)):
	pygame.sprite.Sprite.__init__(self)
	self.type = "person"
	self.image = load_image(image1, -1)
	self.s_image = load_image(image2)
	self.rect = self.s_image.get_rect()
	self.speed = speed
	self.pos_x, self.pos_y = (x, y)
	self.hp = 1
	self.status = "live"
	
	self.s_x = 0
	self.s_y = 0

	#이동 AI 관련 임시 추가 - 변수명은 임시로 수정 바람 / 100109 NalRo9
	self.move = 0 # 0: 정지 / 1 : 걷는중 / 2: 뛰는중
	self.m_timer = 0 # 일정 시간 경과시 모드 변경
	self.m_stop = 0 # 정지해 있는 상태를 유지할 프레임수 (몇프레임이 지나고 움직일것인지)
	self.m_walk = 0 # 걷는 상태를 유지할 프레임수 (몇프레임이 지나고 멈출것인지)
	self.m_x = 0 # 1프레임당 x축으로 움직일 최대 값
	self.m_y = 0 # 1프레임당 y축으로 움직일 최대 값
	self.m_running = 150 # 달리기 상태에서의 x축에 대한 이동속도가 (x * m_running / 150)
	# 0:반응없음
	# 11: 토끼에게서 도망간다 (걷기) / 12: 토끼에게 다가간다 (걷기)
	# 21: 도망간다 (뛰기) / 22: 다가간다 (뛰기)
	self.m_death = 0 # 타인의 죽음에 대하여
	self.m_hurt = 0 # 공격받았을때 대하여
	self.m_rabbit = 0 # 토끼를 인식했을때 대하여
	
    def draw(self, screen, camera):
	self.s_x=self.pos_x-camera.px+self.image.get_width()/2-self.s_image.get_width()/2
	self.s_y=self.pos_y+self.image.get_height()-self.s_image.get_height()/2
	self.rect.x = self.s_x
	self.rect.y = self.s_y

	screen.blit(self.s_image, (self.s_x, self.s_y))
	screen.blit(self.image, (self.pos_x-camera.px, self.pos_y))

    def attacked(self, hitpoint):
	if self.hp > 0:
            self.hp -= hitpoint
	if self.hp <= 0:
	    self.status = "die"
	    print "die"
