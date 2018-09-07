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
        # Интервал изменения переменной по оси X
        self.xmin = -20.0
        self.xmax =  20.0
        # Шаг между точками
        self.dx = 0.01
        #Создадим список координат по оси X
        #на отрезке [-xmin; xmax], включая концы
        self.xlist = mlab.frange (self.xmin, self.xmax, self.dx)
        
        #for i in range(self.xlist.size):
        #    print i, " - ", self.xlist[i]

    def func_sinus (self, x):
        '''  sinc (x) '''
        if x == 0:
            return 1.0
        return math.sin (x) / x

    def draw_sinus(self):
        # Вычислим значение функции в заданных точках
        self.ylist1 = [self.func_sinus (x) for x in self.xlist]
        self.ylist2 = [self.func_sinus (x * 0.2) for x in self.xlist]

        # Нарисуем одномерные графики
        pylab.plot (self.xlist, self.ylist1)
        pylab.plot (self.xlist, self.ylist2)

        # Покажем окно с нарисованным графиком
        pylab.show()
        

    def draw_sinus_move(self):
        

        #Включаем интерактивный режим
        pylab.ion()
        for n in range(25):
            #Данные для очередного кадра
            self.ylist = [math.sin (x + n / 2.0) for x in self.xlist]
            #Очистим график
            pylab.clf()
            #Выведем новые данные
            pylab.plot (self.xlist, self.ylist)
            #Нарисуем их
            pylab.draw()
    print "drawing over! \n"
    pylab.close()

    def draw_sinus_2(self):
        a = 1
        n = 1
        while a>0:
 
            #Данные для очередного кадра
            ylist = [math.sin (x + n / 2.0) for x in xlist]

            #Очистим график
            pylab.clf()

            #Выведем новые данные
            pylab.plot (xlist, ylist)

            #Нарисуем их
            pylab.draw()
     
            n = n+1
        

