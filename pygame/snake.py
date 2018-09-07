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
import pygame
from pygame import *
import random
# from pygame.locals import *

# Define some colors
black = (0,0,0)
white = (255,255,255)
COLOR =  "#888888"
snake_color = (255, 0, 0)
apple_color = (20, 200, 20)

class Apple(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w = 20
        self.h = 20
        self.image = Surface((self.w, self.h))
        self.image.fill(apple_color)
        # self.image.fill(Color(COLOR))
        self.random_position()

    def get_coord(self):
        return self.pos #self.rect.x, self.rect.y

    def random_position(self):
        self.pos = (random.randint(0, 590), random.randint(0, 590))

    def draw(self, screen): # draw myself to screen
        screen.blit(self.image, self.pos)

class Snake(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w = 20
        self.h = 20
        self.snake_img = Surface((self.w, self.h))
        self.snake_img.fill(snake_color)

        self.xs = [190, 190, 190, 190, 190]
        self.ys = [290, 270, 250, 230, 210]

    def get_random_color(self):
        r = random.randint(0, 255) 
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rnd_color = (r, g, b)
        return rnd_color 

    def draw(self, screen):
        for i in range(0, len(self.xs)):
            self.snake_img.fill(self.get_random_color())
            screen.blit(self.snake_img, (self.xs[i], self.ys[i]))
        #end_for

    def wall_collision(self):
        ''' check collision with wall'''
        max_wall = 590
        min_wall = -10
        if (self.xs[0] < min_wall or self.xs[0] > max_wall or self.ys[0] < min_wall or self.ys[0] > max_wall):
            return True
        #endif

    def apple_collision(self, apple_coord_x, apple_coord_y):
        if self.collide(self.xs[0], apple_coord_x, self.ys[0], apple_coord_y, 20, 10, 20, 10):
            self.xs.append(700)
            self.ys.append(700)
            return True
        else:
            return False
        #endif

    def itself_collision(self):
        ''' check collision with itself'''
        i = len(self.xs) - 1
        while i >= 2:
            if self.collide(self.xs[0], self.xs[i], self.ys[0], self.ys[i], 20, 20, 20, 20):
                # die(screen, score)
                return True
            #endif
            i-= 1
        #end_while
        return False

    def refresh(self):
        i = len(self.xs) - 1
        while i >= 1:
            self.xs[i] = self.xs[i-1]
            self.ys[i] = self.ys[i-1]
            i -= 1
        #end_while

    def change_dir(self, dirs):
        delta = 20
        if dirs == 0:
            self.ys[0] += delta
        elif dirs == 1:
            self.xs[0] += delta
        elif dirs == 2:
            self.ys[0] -= delta
        elif dirs== 3:
            self.xs[0] -= delta

    def collide(self, x1, x2, y1, y2, w1, w2, h1, h2):
        if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
            return True
        else:
            return False
        #endif

def die(screen, score):
    f=pygame.font.SysFont('Arial', 30)
    t=f.render('Your score was: '+str(score), True, (0, 0, 0))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(500)
    sys.exit(0)


if __name__ == "__main__":

    print "Main program start."
    print "Python version: "
    print sys.version
    print "----------------------\n"
    main_scr_pos_x = 200
    main_scr_pos_y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (main_scr_pos_x, main_scr_pos_y)

    dirs = 0
    score = 0

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Snake')

    f = pygame.font.SysFont('Arial', 20)
    clock = pygame.time.Clock()

    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(10)
        for e in pygame.event.get():

            if e.type == QUIT:
                sys.exit(0)
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit(0)
            elif e.type == KEYDOWN:
                if e.key == K_UP and dirs != 0:
                    dirs = 2
                elif e.key == K_DOWN and dirs != 2:
                    dirs = 0
                elif e.key == K_LEFT and dirs != 1:
                    dirs = 3
                elif e.key == K_RIGHT and dirs != 3:
                    dirs = 1
                #endif
            #endif
        #end_for
        
        # check collision with itself:
        if snake.itself_collision():
            die(screen, score)
        #endif

        #collide = pygame.sprite.spritecollide(snake, apple, False)
        #if collide:
        #    print "Collide with an apple!"
        #endif

        #check collision with wall:
        if snake.wall_collision():
            die(screen, score)
        #endif

        #check collision with apple:
        if snake.apple_collision(apple.get_coord()[0], apple.get_coord()[1]):
            # snake increase itself
            score+=1
            # create new apple:
            apple = Apple()
        #endif

        # snake rearrange:
        snake.refresh()
        
        #snake choose direction:
        snake.change_dir(dirs)

        screen.fill((255, 255, 255))

        #draw snake:
        snake.draw(screen)

        #draw apple:
        apple.draw(screen)

        txt_score=f.render(str(score), True, (0, 0, 0))
        screen.blit(txt_score, (10, 10))

        pygame.display.update()
    #end_while
    print "Main program ends"
