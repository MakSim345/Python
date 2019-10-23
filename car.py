#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date
import hashlib

from xml.dom import minidom


class Vehicle:
    def __init__ (self, color, model):
        self.color = color
        self.model = model
    #end_def    

class Device:
    def __init__(self):
        self._voltage = 12
    #end_def        

class Car (Vehicle, Device):
    def __init__(self, color, model, year):
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year
    #end_def


class Car (Vehicle, Device):
    def __init__(self, color, model, year):
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year
    #end_def    
    
    @property
    def voltage (self):
        return self._voltage
    #end_def
    
    @voltage.setter
    def voltage(self, volts):
        print ("Warning: this can cause problems!")
        self._voltage = volts
    #end_def    
    
    @voltage.deleter
    def voltage(self, volts):
        print ("Warning: this can cause problems!")
        del self._voltage
    #end_def    


class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0

def calc_md5(_filename):
    # os.system("taskkill /im Genied.exe /f")
    exec_line = "md5sum.exe " + _filename + " \n"
    # print "To run:", exec_line
    # os.system(exec_line)
    resultMD5 = hashlib.md5(open(_filename).read()).hexdigest()
    return resultMD5

def calc_md5_exe(_filename):
    import subprocess
    exec_line = "md5sum " + _filename #  + " \n"
    # "md5sum gmail.csv"
    # _filename = _filename + " \n"
    # os.system(exec_line)
    #resultMD5 = subprocess.Popen(["md5sum.exe", _filename], stdout=subprocess.PIPE).communicate()[0]
    # resultMD5 = subprocess.Popen(["md5sum.exe", _filename], stdout=subprocess.PIPE).communicate()[0]
    p = subprocess.Popen(exec_line, shell=True, stdout=subprocess.PIPE)
    resultMD5, filename = p.communicate()[0].split()
    # print "calc_md5_exe:", _filename, resultMD5
    return resultMD5


    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    
    print ""
    print "Main program end."

