#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import sys, traceback
import pylab
import random
from matplotlib import mlab

class drawSinus():
    def __init__(self, name='drawSinus'):
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
            y = random.randrange(3, 35, 1) # Even number from 3 to 35
            # self.ylist = [math.sin (x + n / 2.0) for x in self.xlist]
            self.ylist = [random.randrange(3, 350, 1) for x in self.xlist]
            # print self.ylist
            
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
       

       # main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""

    my_sin = drawSinus()
    my_sin.draw_sinus_move()
    print ""
    print "Main program ends"
