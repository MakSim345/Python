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
import random
import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height):
    # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Make a blue wall, of the size specified in the parameters        
        self.w = width
        self.h = height
        self.refresh_img()
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def resize(self):
        self.w = self.w + 10
        width = self.w
        height = self.h
        self.refresh_img()

    def refresh_img(self):
        print "width=", self.w
        self.image = pygame.Surface([self.w, self.h])
        self.image.fill(blue)
        

class Bricket(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height):
    # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
