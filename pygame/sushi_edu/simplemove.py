#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os
import traceback
import sys
import pygame
from pygame.locals import *

class SushiPlate():
    ''' '''
    def __init__(self):
        ''' '''
        # super(ClassName, self).__init__()
        # self.arg = arg


    def run(self):
        ''' '''
        print "I'm runnung!"
        background_image_filename = 'sushiplate.jpg'
        sprite_image_filename = 'fugu.png'
        pygame.init()
        screen = pygame.display.set_mode((640, 480), 0, 32)
        background = pygame.image.load(background_image_filename).convert()
        sprite = pygame.image.load(sprite_image_filename)

        # the coordinate of our sprite:
        x = 0

        while True:
            for event in pygame.event.get():
                if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    sys.exit(0)
                else:
                    pass
                #endif
            #end_for
            screen.blit(background, (0,0))
            screen.blit(sprite, (x, 100))
            x += 10.
            # if the image goes off the end of the screen, move it back:
            if x >640.:
                x -= 640.
            #endif

            pygame.display.update()
        #end_while



if __name__ == "__main__":

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        sp = SushiPlate()
        sp.run()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()


    print "Main program ends"
