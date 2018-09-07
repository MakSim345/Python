#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
from drawSinus import *
from drawHistogram import *

# main entrance point:
if __name__ == "__main__":    

    print "Main program begins"
    print ""

    #my_sin = drawSinus()
    #my_sin.draw_sin()
    #my_sin.draw_sinus_move()

    my_hist = drawHistogram()
    # my_hist.draw_hist_vybory(10000, 10000)
    my_hist.draw_hist_vybory2()

    print ""    
    print "Main program ends"
