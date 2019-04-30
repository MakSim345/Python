#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import string
import os
import time
import sys, traceback
from datetime import date
from random import random

def inCircle(x, y):
	return x*x + y*y < 1.0

def pi_calc_02(trials):
    inside = 0
    for i in xrange(trials):
        x = random()
        y = random()
        # if x*x + y*y < 1.0:
        if inCircle(x, y):
            inside += 1
    return 4.0 * inside / trials

def pi_calc_01():
    _sum = 0
    i = 0
    n =0
    delit = 1
    PI = 0.0

    # print("n=")
    #scanf("%I64u",&n)
    n = input ("Enter a non-negative integer to iterations of PI calculation: ")

    for i in range(n):
        # _sum += (1.0/(1.0+2.0*i))*((i%2==0) ? 1:(-1))
        if (i%2 == 0):
            PI = PI + 4.0/delit;
        else:
            PI = PI - 4.0/delit;
        #endif

        delit = delit + 2;
    #end for

    _sum*=4;
    # print "_sum=", _sum
    print "PI=", PI

def factorial_calc(num_to_calc):
    '''Function calculate a factorial '''
    product = 1

    for i in range(num_to_calc):
        product = product * (i + 1)
        print i, " - ", product
    #end_for
#end_def

def power_of_two(num_to_calc):
    '''Function calculate a power of 2 '''
    product = 1

    for i in range(num_to_calc):
        product = pow(2, i)
        print "2^" + str(i) + " -", product
    #end_for
#end_def

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0


    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #number = input ("Enter a non-negative integer to take factorial of: ")
    #factorial_calc(number)

    number = input ("Enter a non-negative integer: ")
    print pi_calc_02(number)
    # pi_calc_01()

    print ""
    print "Main program end."

