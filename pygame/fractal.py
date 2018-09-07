#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# http://programarcadegames.com/

#############################################################################
##
##
#############################################################################

import sys, os  
import traceback
import pygame
  
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

class Fractal():
    def __init__(self):
        ''' '''
        self.init_window()


    def init_window(self):
        pygame.init()
   
        # Set the height and width of the screen
        size = [700,700]
        self.screen = pygame.display.set_mode(size)
  
        pygame.display.set_caption("My Game")
  
        #Loop until the user clicks the close button.
        done = False
  
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def input(self, events):
        for event in events:
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
            else:
                pass

    def run(self):
        # -------- Main Program Loop -----------
        while 1:
            self.input(pygame.event.get())
            
            # Set the screen background
            self.screen.fill(white)
      
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            fractal_level = 5
            self.recursive_draw(0, 0, 700, 700, fractal_level)
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
            # Limit to 20 frames per second
            self.clock.tick(20)
      
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        #end_while

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()

    #end_def    
    def recursive_draw(self, x, y, width, height, count):
        # Draw the rectangle
        #pygame.draw.rect(screen,black,[x,y,width,height],1)
        pygame.draw.line(self.screen,
                     black,
                     [x+width*.25,height//2+y],
                     [x+width*.75,height//2+y],
                     3)
        pygame.draw.line(self.screen,
                     black,
                     [x+width*.25,(height*.5)//2+y],
                     [x+width*.25,(height*1.5)//2+y],
                     3)
        pygame.draw.line(self.screen,
                     black,
                     [x+width*.75,(height*.5)//2+y],
                     [x+width*.75,(height*1.5)//2+y],
                     3)
 
        if count > 0:
            count -= 1
            # Top left
            self.recursive_draw(x,y,                    width//2,height//2,count)
            # Top right
            self.recursive_draw(x+width//2,y,           width//2,height//2,count)
            # Bottom left
            self.recursive_draw(x,y+width//2,           width//2,height//2,count)
            # Bottom right
            self.recursive_draw(x+width//2,y+width//2,  width//2,height//2,count)
        #endif    
    #end_def    
 
if __name__ == '__main__': 
    
    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        fractal = Fractal()
        fractal.run()        
        # TimeTest001()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"
