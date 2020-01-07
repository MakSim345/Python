#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# ============================================================
#
# NOV-2019.
# YS. 
# ============================================================

from time import time


if __name__ == "__main__":

    print "Main program begins"
    print ""

    start_time = time()
    
    for i in range (1, 1001):
        print (i)
    #end for

    end_time = round (time() - start_time, 3)

    print (str(end_time) + "ms")

    print ""
    print "Main program ends"


