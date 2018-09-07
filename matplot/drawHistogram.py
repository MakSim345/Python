#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.ticker import EngFormatter

class drawHistogram():
    '''Make a histogram of normally distributed random numbers and plot the
       analytic PDF over it'''

    def __init__(self):
        '''_'''

    def draw_hist_vybory(self, nMax = 10000, people = 1000):
        '''-'''
        my_arr = []
        persent = 100
        votes_in_persent = 0
        my_arr.append(votes_in_persent)

        for i in range(nMax):
            vbros = 0
            bullets=np.random.randint(1, people)
            # bullets=people
            divirgent = (bullets/100)*5
            if (divirgent <= 0):
                votes = (bullets/2)
            else:
                vbros = np.random.randint(0, (bullets/100)*15)
                #vbros = np.random.randint(0, (people/100)*15)
                votes = (bullets/2 + np.random.randint(0, divirgent)
                                   - np.random.randint(0, divirgent)
                                   + np.random.randint(0, divirgent))
            
            votes_in_persent = ((votes*100)/bullets) #+ vbros
            # print "\ny4acTok HOMep: ", i
            #print "\n"
            #print "koL-Bo 6I0LLeT: ", bullets, ". noMex: ", divirgent
            #print "koL-Bo roLocoB: ", votes, ". B % =", votes_in_persent
            #print "B6poc:", vbros
            
            
            my_arr.append(votes_in_persent)
            # my_arr.append(votes + vbros)

        num_to_show = 100
        # my_arr.append(100)
        plt.hist(my_arr, num_to_show, color = 'green')
        plt.grid(True)
        #my_arr.sort()
        #print my_arr
        plt.show()

    def draw_hist_vybory2(self, nMax = 10000, people = 1000):        
        '''
        Demo to show use of the engineering Formatter.
        '''
        my_arr = []
        persent = 100
        votes_in_persent = 0
        my_arr.append(votes_in_persent)

        for i in range(nMax):
            vbros = 0
            bullets=np.random.randint(1, people)
            # bullets=people
            divirgent = (bullets/100)*5
            if (divirgent <= 0):
                votes = (bullets/2)
            else:
                vbros = np.random.randint(0, (bullets/100)*15)
                #vbros = np.random.randint(0, (people/100)*15)
                votes = (bullets/2 + np.random.randint(0, divirgent)
                                   - np.random.randint(0, divirgent)
                                   + np.random.randint(0, divirgent))
            
            votes_in_persent = ((votes*100)/bullets) #+ vbros
            # print "\ny4acTok HOMep: ", i
            #print "\n"
            #print "koL-Bo 6I0LLeT: ", bullets, ". noMex: ", divirgent
            #print "koL-Bo roLocoB: ", votes, ". B % =", votes_in_persent
            #print "B6poc:", vbros
            
            
            my_arr.append(votes_in_persent)
            # my_arr.append(votes + vbros)

        num_to_show = 100
        fig = plt.figure()
        # ax = fig.add_subplot(111)
        plt.plot(my_arr)

        plt.show()
        

    def draw_hist1(self, nMax = 1000):
        '''-'''
        y = np.random.randn(nMax)
        plt.hist(y, nMax/10, color = 'green')
        plt.show()

    def draw_hist2(self):
        mu = 100
        sigma = 15

        x = mu + sigma * np.random.randn(10000)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # the histogram of the data
        n, bins, patches = ax.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

        # hist uses np.histogram under the hood to create 'n' and 'bins'.
        # np.histogram returns the bin edges, so there will be 50 probability
        # density values in n, 51 bin edges in bins and 50 patches.  To get
        # everything lined up, we'll compute the bin centers
        bincenters = 0.5*(bins[1:]+bins[:-1])
        # add a 'best fit' line for the normal PDF
        y = mlab.normpdf( bincenters, mu, sigma)
        l = ax.plot(bincenters, y, 'r--', linewidth=1)

        ax.set_xlabel('Smarts')
        ax.set_ylabel('Probability')
        #ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
        ax.set_xlim(40, 160)
        ax.set_ylim(0, 0.03)
        ax.grid(True)

        plt.show()

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

