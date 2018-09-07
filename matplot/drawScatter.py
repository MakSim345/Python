#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np

class drawScatter():
    def __init__(self, name='drawScatter'):
        print name, 'started!\n'
        self.x = np.random.randn(1000)
        self.y = np.random.randn(1000)
 
        self.size = 50*np.random.randn(1000)
        self.colors = np.random.rand(1000)
 
        
        
    def func_sinus (self, x):
        '''  sinc (x) '''
        if x == 0:
            return 1.0
        return math.sin (x) / x

    def draw_scatter(self):
        plt.scatter(self.x, self.y, s=self.size, c=self.colors)
        plt.show()
     
