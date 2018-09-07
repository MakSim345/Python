#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import string
import os
import time
import sys, traceback
from datetime import date
import pickle
import urllib2

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

    number = input ("Enter a non-negative integer to show max power of 2: ")
    power_of_two(number)
    
    print ""    
    print "Main program end."

