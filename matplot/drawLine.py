#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt

class drawLine():
    def __init__(self, name='drawLine'):
        print name, 'started!\n'

    def draw_line(self):
        plt.plot([1,2,3])
        plt.ylabel('some numbers')
        plt.show()
       

class drawLine_():
    def __init__(self, name='drawLine_'):
        print name, 'started!\n'
        # �������� ��������� ���������� �� ��� X
        self.xmin = -20.0
        self.xmax =  20.0
        # ��� ����� �������
        self.dx = 0.01
        #�������� ������ ��������� �� ��� X
        #�� ������� [-xmin; xmax], ������� �����
        self.xlist = mlab.frange (self.xmin, self.xmax, self.dx)
        
        #for i in range(self.xlist.size):
        #    print i, " - ", self.xlist[i]

    def func_sinus (self, x):
        '''  sinc (x) '''
        if x == 0:
            return 1.0
        return math.sin (x) / x

    def draw_sinus(self):
        # �������� �������� ������� � �������� ������
        self.ylist1 = [self.func_sinus (x) for x in self.xlist]
        self.ylist2 = [self.func_sinus (x * 0.2) for x in self.xlist]

        # �������� ���������� �������
        pylab.plot (self.xlist, self.ylist1)
        pylab.plot (self.xlist, self.ylist2)

        # ������� ���� � ������������ ��������
        pylab.show()
        

    def draw_sinus_move(self):
        

        #�������� ������������� �����
        pylab.ion()
        for n in range(25):
            #������ ��� ���������� �����
            self.ylist = [math.sin (x + n / 2.0) for x in self.xlist]
            #������� ������
            pylab.clf()
            #������� ����� ������
            pylab.plot (self.xlist, self.ylist)
            #�������� ��
            pylab.draw()
    print "drawing over! \n"
    pylab.close()

    def draw_sinus_2(self):
        a = 1
        n = 1
        while a>0:
 
            #������ ��� ���������� �����
            ylist = [math.sin (x + n / 2.0) for x in xlist]

            #������� ������
            pylab.clf()

            #������� ����� ������
            pylab.plot (xlist, ylist)

            #�������� ��
            pylab.draw()
     
            n = n+1
        

