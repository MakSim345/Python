import math
import string
import os
import sys, traceback
import matplotlib.pyplot as plt
import numpy as np

class myClass():
    def __init__(self, name):
        print 'myClass started! with name', name
        
    
class drawHist(Exception):
    def __init__(self):
        print "drawHist - init"
    
    def draw_hist_1(self):
        '''-''' 
        y = np.random.randn(1000) 
        plt.hist(y, 25)
        plt.show()

        
