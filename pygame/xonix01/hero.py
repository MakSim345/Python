#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
from pygame import *

MOVE_SPEED = 7
WIDTH = 10
HEIGHT = 10
COLOR =  "#888888"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #speed of moving. 0 = stays on place
        self.yvel = 0   #speed of moving. 0 = stays on place
        self.startX = x # start position. For future use
        self.startY = y

        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        
        self.rect = Rect(x, y, WIDTH, HEIGHT) # rectangle

    def update(self, left, right, up, down):
        if left:
            self.xvel = -MOVE_SPEED # left = x- n
        #endif 
        if right:
            self.xvel = MOVE_SPEED # Right = x + n
        #endif 
        if up:
            self.yvel = -MOVE_SPEED # 
        #endif 
        if down:
            self.yvel = MOVE_SPEED # 
        #endif 
        if not(left or right or up or down): # do nothing
            self.xvel = 0
            self.yvel = 0
        #endif 

        self.rect.x += self.xvel # transfer itself to xvel position
        self.rect.y += self.yvel # transfer itself to yvel position

    def get_coordinates(self):
        return self.rect.x, self.rect.y

    def draw(self, screen): # draw myself to screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
