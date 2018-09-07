#!/usr/bin/env python

#############################################################################
##
## Coursera Oct-2012. Labs number 1 and 2.
##
#############################################################################

import math
import sys, os
import random


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

print count_polygon(7, 3)

