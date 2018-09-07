#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import time
import sys, traceback

def convert(num_to_convert):
    '''Function convert pixels to virtual coordinates for ESP '''
    return (num_to_convert * 100) / 8.0
#end def

    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    if len(sys.argv)<2:
        print "Program needs a parameter!"
    else:
        to_convert = float(sys.argv[1])
        print "Convert", sys.argv[1], "pixels to virtual coordinates:"
        print convert(to_convert)
    #endif

    print ""    
    print "Main program end."

