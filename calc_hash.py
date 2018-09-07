#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date
import hashlib

from xml.dom import minidom

def factorial_calc(num_to_calc):
    '''Function calculate a factorial '''
    product = 1

    for i in range(num_to_calc):
        product = product * (i + 1)
        print i, " - ", product
    #end_for
#end_def

def power_of_two(num_to_calc):
    '''Function calculate a power of 2 '''
    product = 1

    for i in range(num_to_calc):
        product = pow(2, i)
        print "2^" + str(i) + " -", product
    #end_for
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
    
    file_1 = "1.xml"

    xmldoc = minidom.parse(file_1)

    itemlist = xmldoc.getElementsByTagName('item')

    print(len(itemlist))

    print(itemlist[0].attributes['name'].value)

    for s in itemlist:
        print(s.attributes['name'].value)
    
    print ""
    print "Main program end."

