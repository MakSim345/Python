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

def TimeTest001():
    # time.clock() gives wallclock seconds accurate to at least 1 millisecond
    # it updates every millisecond, but only works with windows
    # time.time() is more portable, but has quantization errors
    # since it only updates updates 18.2 times per second
    import time
    print "\nTiming a 1 million loop 'for loop' ..."
    start = time.clock()
    
    for x in range(1000000):
        y = 100*x - 99 # do something
    #end_for
        
    end = time.clock()
    print 'start', start
    print 'end', end
    print "Time elapsed = ", end - start, "seconds"
    """
    result -->
    Timing a 1 million loop 'for loop' ...
    Time elapsed = 0.471708415107 seconds
    """
def TimeTest002():
    import time
    import sys
    print sys.getcheckinterval()
    for i in range (100):
         # now = time.time()
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now
    print 'STOP'

def TimeTest003():
    import time
    import sys
    import arrays

    for i in range (10):
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now, "QT: ", m_ms.elapsed()

    print 'STOP'

def SaveStatus(data_to_save):
    import pickle, time, sys
    # mydata = ("abc", 12, [1, 2, 3])
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.dump(data_to_save)
    output_file.close()

def ReadStatus():
    import pickle, time, sys
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.get(data_to_save)
    output_file.close()

class MyClass():
    def __init__(self):
        self.a = 100
        self.__b = 200
        
    def dump(self):    
        print "My value a = ", self.a

    def dump_b(self):
        '''test private member'''
        print "My value __b = ", self.__b

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

        self.image = Surface((WIDTH,HEIGHT))
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
   
    def draw(self, screen): # draw myself to screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

class xonix():
    def __init__(self):
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 640
        # self.DISPLAY = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.DISPLAY = (800, 640)
        self.BACKGROUND_COLOR = "#004400"
        self.hero = Player(55,55) 
        self.left = self.right = False 
        self.up = self.down = False 
        self.timer = time.Clock()

    def run(self):
        init()
        screen = display.set_mode(self.DISPLAY)
        display.set_caption("xonix")
        #bg = Surface(self.WIN_WIDTH, self.WIN_HEIGHT)
        bg = Surface((self.DISPLAY))
        bg.fill(Color(self.BACKGROUND_COLOR))
        
        # draw.line(bg, (10,100,100),(10,200),(20,300),2)
        
        while 1:
            self.timer.tick(60)
            for e in event.get():
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit ,"QUIT"
                #endif                    
                if e.type == QUIT:
                    raise SystemExit ,"QUIT"
                #endif
                if e.type == KEYDOWN and e.key == K_LEFT:
                    self.left = True
                #endif
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    self.right = True
                #endif
                if e.type == KEYUP and e.key == K_RIGHT:
                    self.right = False
                #endif
                if e.type == KEYUP and e.key == K_LEFT:
                    self.left = False
                #endif

                if e.type == KEYDOWN and e.key == K_UP:
                    self.up = True
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

            screen.blit(bg, (0,0))    
            
            self.hero.update(self.left, self.right, self.up, self.down) 
            self.hero.draw(screen) 
            display.update()
            #endfor        
         #endwhile
            
if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        sm = xonix()
        sm.run()        
        # TimeTest001()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"

