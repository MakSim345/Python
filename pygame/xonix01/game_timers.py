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
from hero import *
from enemy import *

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

