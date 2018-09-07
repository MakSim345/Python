#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import pygame

number = 5
black = 0, 0, 0

class MyClass():
    def __init__(self):
        self.a = 100
        self.__b = 200
        
    def dump(self):    
        print "My value a = ", self.a

    def dump_b(self):
        '''test private member'''
        print "My value __b = ", self.__b

class PingPong():
    def __init__(self):
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 640
        # self.DISPLAY = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.DISPLAY = (800, 640)
        self.BACKGROUND_COLOR = "#004400"
        

    def run(self):
        pygame.init()
        self.speed = [2, 2]
        screen = pygame.display.set_mode(self.DISPLAY)
        pygame.display.set_caption("Ping-Pong pygame")
        self.ball = pygame.image.load('ball.jpg')
        self.ballrect = self.ball.get_rect()

        #bg = pygame.Surface((self.DISPLAY))
        #bg.fill(pygame.Color(self.BACKGROUND_COLOR))

        while 1:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit ,"QUIT"
                #endif
                
            self.ballrect.move(self.speed)
            
            if self.ballrect.left < 0 or self.ballrect.right > self.WIN_WIDTH:
                self.speed [0] = -self.speed [0]

            if self.ballrect.top < 0 or self.ballrect.bottom > self.WIN_HEIGHT:
                self.speed [1] = -self.speed [1]

            screen.fill (black)
            
            screen.blit(self.ball, self.ballrect)    
            pygame.display.flip()
            #endfor        
         #endwhile
            
if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        sm = PingPong()
        sm.run()        
        # TimeTest001()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"

