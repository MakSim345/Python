import string
import os
import sys, traceback
from drawHysto import *
from drawSinus import *
from drawScatter import *
from drawLine import *
# main entrance point:
if __name__ == "__main__":    

    print "Main program begins"
    print ""

    #_my_hist = drawHist()
    #_my_hist.draw_hist_1()

    #_my_sinus = drawSinus()
    #_my_sinus.draw_sinus()

    #_my_scatter = drawScatter()
    #_my_scatter.draw_scatter()

    _my_line = drawLine()
    _my_line.draw_line()
    
    print ""    
    print "Main program ends"
