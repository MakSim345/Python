#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
import math
from matplotlib import pylab
from matplotlib import mlab

def MyArray():
    a = [676.7, 353, 433, 14, 14.565]
    # a.sort()
    # print a
    return a

def sorter():
    lines = sys.stdin.readlines()
    lines.sort()
    for i in lines:
        print i
    
class myAbstractClass():
    def __init__(self, name='default'):
        raise NotImplementedError, "Must subclass me"
        # print 'myAbstractClass started! with name', name

class drawSinus():    
    def __init__(self, nMin = -10.0, nMax = 10.0, nDx = 0.01):
        #min/max values:
        self.xmin = nMin
        self.xmax = nMax
        # step between points:
        self.dx = nDx
        self.crease_coord_points()
        print "init complete"

    def crease_coord_points(self):
        self.xlist = mlab.frange (self.xmin, self.xmax, self.dx)
        self.ylist = [self.func_sin (x) for x in self.xlist]

    def func_sin (self, x):
        """  sin (x)  """
        return math.sin (x)

    def draw_sin(self):
        #Нарисуем одномерный график
        pylab.plot (self.xlist, self.ylist)

        #Покажем окно с нарисованным графиком
        pylab.show()

# main entrance point:
if __name__ == "__main__":    

    print "Main program begins"
    print ""

    my_sin = drawSinus()
    my_sin.draw_sin()
    print ""    
    print "Main program ends"
