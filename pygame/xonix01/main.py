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
from hero import *
from enemy import *
from wall import *

class xonix():
    def __init__(self):
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 640
        self.wall_dim = 10
        self.DISPLAY = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.BACKGROUND_COLOR = "#004400"
        self.init_objects()
        self.init_screen()
        self.left = self.right = False
        self.up = self.down = False
        self.init_timer()
    #end_def

    def init_screen(self):
        pygame.init() #pygame.init()
        self.screen = display.set_mode(self.DISPLAY)
        display.set_caption("xonix")
        #bg = Surface(self.WIN_WIDTH, self.WIN_HEIGHT)
        self.bg = Surface((self.DISPLAY))
        self.bg.fill(Color(self.BACKGROUND_COLOR))

    def init_objects(self):
        self.hero = Player(55, 55)
        self.enemy_1 = Enemy()
        self.enemy_2 = Enemy()
        self.entities = pygame.sprite.Group()
        self.build_walls()

    def init_timer(self):
        self.timer = time.Clock()        

    def build_walls(self):
        # Make the walls. (x_pos, y_pos, width, height)
        self.wall_list = pygame.sprite.Group()
        # make perimeter:
        wall = Wall(0, 0, self.WIN_WIDTH, self.wall_dim)
        self.wall_list.add(wall)

        wall = Wall(0, self.WIN_HEIGHT - self.wall_dim, self.WIN_WIDTH, self.wall_dim)
        self.wall_list.add(wall)

        wall = Wall(0, 0, self.wall_dim, self.WIN_HEIGHT)
        self.wall_list.add(wall)

        wall = Wall(self.WIN_WIDTH-self.wall_dim, 0, self.wall_dim, self.WIN_HEIGHT)
        self.wall_list.add(wall)

        # end of perimeter making

        # Build random walls:
        #vertical:

        wall = Wall(500, 0, self.wall_dim, 200)
        self.wall_list.add(wall)

        wall = Wall(200, 200, self.wall_dim, 150)
        self.wall_list.add(wall)

        #Horizontal
        wall = Wall(100, 200, 300, self.wall_dim)
        self.wall_list.add(wall)

        wall = Wall(500, 400, 400, self.wall_dim)
        self.wall_list.add(wall)

        wall = Wall(100, 500, 300, self.wall_dim)
        self.wall_list.add(wall)

    def build_bricket_walls(self, brick_x, brick_y):
        # Make the walls. (x_pos, y_pos, width, height)
        self.brickets_list = pygame.sprite.Group()
        #vertical:
        #wall = Wall(0, 0, 10, 700)
        #self.wall_list.add(wall)

        #wall = Wall(790, 0, 10, 700)
        #self.wall_list.add(wall)

        #wall = Wall(200, 300, 10, 150)
        #self.wall_list.add(wall)

        #Horizontal
        #wall = Wall(0,0,500,10)
        #self.wall_list.add(wall)

        #wall = Wall(100,200,500,10)
        #self.wall_list.add(wall)

        #wall = Wall(200, 500, 700,10)
        #self.wall_list.add(wall)

    def set_timer_delay(self, _tick = 60):
        ''' set delay for correct FPS '''
        self.timer.tick(_tick)

    def run(self):
        
        # draw.line(bg, (10,100,100),(10,200),(20,300),2)
        key_block = False

        _move_wall = Wall(100, 350, 100, 10)
        self.wall_list.add(_move_wall)

        self.entities.add(self.hero)
        self.entities.add(self.enemy_1)
        self.entities.add(self.enemy_2)
        self.entities.add(self.wall_list)
        self.entities.add(_move_wall)

        while 1:
            self.set_timer_delay(60)
            for e in event.get():
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit ,"QUIT"
                #endif
                if e.type == QUIT:
                    raise SystemExit ,"QUIT"
                #endif

                if e.type == KEYDOWN and e.key == K_LEFT:
                    self.left = True
                    # _move_wall.rect.x = _move_wall.rect.x - 10                    
                #endif
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    self.right = True
                    # _move_wall.rect.x = _move_wall.rect.x + 10
                    _move_wall.resize()
                #endif
                if e.type == KEYUP and e.key == K_RIGHT:
                    self.right = False
                #endif
                if e.type == KEYUP and e.key == K_LEFT:
                    self.left = False
                #endif

                if e.type == KEYDOWN and e.key == K_UP:
                    self.up = True
                    key_block = True
                #endif
                if e.type == KEYDOWN and e.key == K_DOWN:
                    self.down = True
                #endif
                if e.type == KEYUP and e.key == K_DOWN:
                    self.down = False
                #endif
                if e.type == KEYUP and e.key == K_UP:
                    self.up = False
                #endif

            self.screen.blit(self.bg, (0,0))

            self.hero.update(self.left, self.right, self.up, self.down)
            # print self.hero.get_coordinates()
            # self.hero.draw(screen)
            if 1:# key_block:
                self.enemy_1.update(self.wall_list)
                self.enemy_2.update(self.wall_list)
                key_block = False

            self.entities.draw(self.screen)

            #collide = pygame.sprite.spritecollide(self.enemy, self.wall_list, False)

            #if collide:
            #   print "collide with wall!"
                #print map(str, collide)
                #for index, item in enumerate(collide):
                #    print "x=", item.rect.x, "y=", item.rect.y
                #pass
            #endif
            display.update()
            #endfor
         #endwhile

if __name__ == "__main__":

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"
    main_scr_pos_x = 200
    main_scr_pos_y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (main_scr_pos_x, main_scr_pos_y)

    try:
        xonix_game = xonix()
        xonix_game.run()
        # TimeTest001()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()


    print "Main program ends"

