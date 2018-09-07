#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
## Coursera Oct-2012/2014. Labs number 1 and 2.
##
#############################################################################

import math
import sys, os
import random
import traceback
# Mystery computation in Python
# Takes input n and computes output named result

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# global state


def getArray():
    a = []
    for i in range(1000):
      tmp = random.randrange(0, 999)
      a.append(tmp)    
    return a
   
# print getArray()

def foo(_value = 0):
    retval = 0
    fg = math.pow(_value, 5)
    print _value, "in power of ", 5, " = ", fg
    tg = math.pow(_value, 2)    
    retval = (-5 * fg) + (69 * tg) - 47
    return retval

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    tmp =  math.pow((1 + rate_per_period),  periods) 
    _future_value = present_value * tmp
    return _future_value

# print "$1000 at 2% compounded daily for 3 years yields $", future_value(500, .04, 10, 10)
# print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
# 1061.8348

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x**2 + point_y**2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
# project_to_distance(2, 7, 4)
# 3.8460
def count_polygon(_number_of_sides, _side_len):
    quoter = 1.0/4.0
    _number_of_sides
    _side_len

    top = quoter * _number_of_sides * math.pow(_side_len, 2)
    bottom = math.tan(math.pi / _number_of_sides)
    retval = top/bottom
    return retval



result = 1
a = []
max_iterations = 10

# helper functions

def init(start):
    '''Initializes n.'''
    global result
    result = start
    print "Input is", result
    
def get_next(current):
    ''' Computation:
        - divide by two if the number is even ,or
        - multiply by 3 and add 1 if the number is odd.
    '''
    retVal = 0
    if (result%2==0):
        retVal = result / 2
    else:
        retVal = (result * 3) + 1

    return retVal

# timer callback

def update():
    ''' Part of mystery computation.'''
    global a
    global result
    
    # Stop iterating after max_iterations
    if result <= 1:
        timer.stop()
        # print "Output is", result
        a.sort()
        print "max in array:", a[-1]
    else:
        result = get_next(result)
        print "tmp: ", result
        a.append(result)


# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""
    #print count_polygon(7, 3)
    # register event handlers
    timer = simplegui.create_timer(10, update)

    # start program
    init(217)
    timer.start()


    print ""
    print "Main program ends"


