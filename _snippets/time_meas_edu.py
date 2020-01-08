#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# ============================================================
#
# NOV-2019.
# YS. 
# ============================================================
from time import time

def TimeTest001():
    # time.clock() gives wallclock seconds accurate to at least 1 millisecond
    # it updates every millisecond, but only works with windows
    # time.time() is more portable, but has quantization errors
    # since it only updates updates 18.2 times per second
    import time
    a = []
    print "\nTiming a 1 million loop 'for loop' ..."
    start = time.clock()
    for x in range(1000000):
        y = 100*x - 99^99 # do something
        a.append(y) 
    end = time.clock()
    # print a
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
    print "sys.getcheckinterval:", sys.getcheckinterval()
    for i in range (10):
         # now = time.time()
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now
    print 'STOP'


if __name__ == "__main__":

    print "Main program begins"
    print ""

    start_time = time()
    
    for i in range (1, 1001):
        print (i)
    #end for

    end_time = round (time() - start_time, 3)

    print (str(end_time) + "ms")

    TimeTest001()

    print ""
    print "Main program ends"


