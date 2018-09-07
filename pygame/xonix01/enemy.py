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
from wall import *

# Define some colors
black = (0,0,0)
white = (255,255,255)
COLOR =  "#888888"

# This class represents the moving enemy
# It derives from the "Sprite" class in Pygame
class Enemy(pygame.sprite.Sprite):
    # Speed in pixels per cycle
    speed = 0
    # Floating point representation of where the enemy is
    x = 0
    y = 0
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Height and width of the enemy
        self.width = 10
        self.height = 10
        # direction of enemy in degrees
        self.direction = 0
        
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create the image of the enemy:
        self.image = pygame.Surface([self.width, self.height])

        # Color the ball
        self.image.fill(pygame.Color(COLOR))
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
        # Get attributes for the height/width of the screen
        # self.setScreenSizes()
        # self.screenheight = pygame.display.get_surface().get_height()
        # self.screenwidth = pygame.display.get_surface().get_width()
        # Set the initial ball speed and position
        self.reset()

    def setScreenSizes(self, scr_height = 640, scr_width = 800):
        self.screenheight = scr_height
        self.screenwidth = scr_width

    def reset(self):
        self.x = random.randrange(50,750)
        self.y = 350.0
        self.speed = 5.0
        # Direction of ball (in degrees)
        self.direction = random.randrange(-45,45)
        # Flip a 'coin'
        if random.randrange(2) == 0 :
            # Reverse ball direction, let the other guy get it first
            self.direction += 180
            self.y = 50

    # This function will bounce the ball off a horizontal surface (not a vertical one)
    def bounce(self,diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff
        # Speed the ball up
        self.speed *= 1.1

    # Update the position of the object:
    def update(self, wall_list):
        hit_already = False

        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

        # check if we hit any wall:
        collide = pygame.sprite.spritecollide(self, wall_list, False)

        if collide:
            # print "new collide!"
            for index, wall_in_list in enumerate(collide):
                #print "me.top", self.rect.top, "me.bottom", self.rect.bottom
                #print "me.left", self.rect.left, "me.right", self.rect.right
                #print "collide: top", wall_in_list.rect.top, "bottom", wall_in_list.rect.bottom
                #print "left",wall_in_list.rect.left, "right", wall_in_list.rect.right

                # check if wall vertical or horisontal:
                if (wall_in_list.rect.width > wall_in_list.rect.height):
                    if self.rect.top <= wall_in_list.rect.bottom:
                        self.direction = (180-self.direction)%360
                    elif self.rect.bottom >= wall_in_list.rect.top:
                        self.direction = (180-self.direction)%360
                    #endif
                elif (wall_in_list.rect.height > wall_in_list.rect.width):
                    if self.rect.left <= wall_in_list.rect.right:
                        self.direction = (360-self.direction)%360
                    elif self.rect.right >= wall_in_list.rect.top:
                        self.direction = (360-self.direction)%360
                    #endif
                #endif
            #endfor
        #endif

    def draw(self, screen): # draw myself to screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
