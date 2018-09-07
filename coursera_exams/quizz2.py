#!/usr/bin/env python

#############################################################################
##
## Coursera Oct-2012. Labs number 1 and 2.
##
#############################################################################

import math
import sys, os
import random

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    tmp =  math.pow((1 + rate_per_period),  periods) 
    _future_value = present_value * tmp
    return _future_value


def q6():
    '''
    When investing money, an important concept to know is compound interest. 
    The equation FV = PV (1+rate)^periods relates the following four quantities:

    - The present value (PV) of your money is how much money you have now.
    - The future value (FV) of your money is how much money you will have in the future.
    - The nominal interest rate per period (rate) is how much interest you earn during a particular length of time, before accounting for compounding. This is typically expressed as a percentage.
    - The number of periods (periods) is how many periods in the future this calculation is for.
    
    Finish the following code, run it, and submit the printed number.     
    Provide at least four digits of precision after the decimal point.
    
    Before submitting your answer, test your function on the following example. 
    future_value(500, .04, 10, 10) should return 745.317442824.   
    '''
    print "should return 745.317442824: ", future_value(500, .04, 10, 10)    
    print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)


def q5(_argf):
    '''
    Implement the mathematical function 
    f(x) = -5 x^5 + 69 x^2 - 47 
    as a Python function. 
    Then use Python to compute the function values f(0), f(1), f(2), and f(3). 
    Enter the maximum of these four numbers. 
    '''
    retval = 0
    # retval = (-5 * (_argf**5)) + (69 * (_argf**2)) - 47
    retval = (-5 * (math.pow(_argf, 5))) + (69 * (math.pow(_argf, 2))) - 47
    return retval


def getArray():
    a = []
    for i in range(1000):
      tmp = random.randrange(0, 999)
      a.append(tmp)    
    return a
   

def foo(_value = 0):
    retval = 0
    fg = math.pow(_value, 5)
    print _value, "in power of ", 5, " = ", fg
    tg = math.pow(_value, 2)    
    retval = (-5 * fg) + (69 * tg) - 47
    return retval


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

def project_to_distance2(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
# project_to_distance2(2, 7, 4)


# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #number = input ("Enter a non-negative integer to take factorial of: ")
    # print count_polygon(7, 3)
    # print q6()
    project_to_distance2(2, 7, 4)
    print ""    
    print "Main program end."



