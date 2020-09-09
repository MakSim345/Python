#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import turtle
import time
from random import randrange

BREAK_FLAG = False

class MyClass():
    def __init__(self):
        self.a = 100
        self.__b = 200
        
    def dump(self):    
        print "My value a = ", self.a

    def dump_b(self):
        '''test private member'''
        print "My value __b = ", self.__b

class SnakeGame():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title = "Snake with turtle module"
        self.screen.bgcolor ('orange')
        self.screen.setup (650, 650)
        self.screen.tracer (0)

    def run(self):

        print "run"

        # draw a food for the snake
        food = turtle.Turtle()
        food.shape('circle')
        food.penup()
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20)) # 
        self.screen.update()
        #self.screen.mainloop()
        #while 1:
        #    sleep(1)
            #endfor        
        #endwhile
            
if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        sm = SnakeGame()
        sm.run()        
        
        # screen = turtle.Screen()
        # screen.title = "Snake with turtle module"
        # screen.bgcolor ('orange')
        # screen.setup (650, 650)
        # screen.tracer (0)
        turtle.mainloop()

    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"

