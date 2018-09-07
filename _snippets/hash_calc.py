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
    ''' 
    Probably incorrect version, because does not read file properly.
    Use 'rb' for filename open!
    '''
    resultMD5 = hashlib.md5(open(_filename, 'rb').read()).hexdigest()
    print "Python hashlib.md5: \t", resultMD5
    return resultMD5

def calc_md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    print "Python 2 hashlib.md5: \t", hash.hexdigest()        
    return hash.hexdigest()


def calc_md5_exe(_filename):
    '''
    Echo appends a \n since you usually do not want lines not ending with a linebreak in your shell 
    (it looks really ugly if the prompt does not start at the very left).
    Use the -n argument to omit the trailing linebreak and it will print the 
    same checksum as your python script:
        > echo -n mystringforhash | md5sum
        86b6423cb6d211734fc7d81bbc5e11d3  -
    '''    
    import subprocess
    exec_line = "md5sum " + _filename #  + " \n"
    # "md5sum gmail.csv"
    # _filename = _filename + " \n"
        # os.system(exec_line)
    # os.system("taskkill /im Genied.exe /f")
    # exec_line = "md5sum.exe " + _filename + " \n"
    # print "To run:", exec_line
    # os.system(exec_line)
    #resultMD5 = subprocess.Popen(["md5sum.exe", _filename], stdout=subprocess.PIPE).communicate()[0]
    # resultMD5 = subprocess.Popen(["md5sum.exe", _filename], stdout=subprocess.PIPE).communicate()[0]
    p = subprocess.Popen(exec_line, shell=True, stdout=subprocess.PIPE)
    resultMD5, filename = p.communicate()[0].split()
    print "System calc md5.exe: \t", resultMD5
    return resultMD5


    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    file_1 = "new_dropbox_db.csv"
    # file_1 = "main.cpp"
    print "Calculate hash for file '"+ file_1+ "':" 
    calc_md5_exe(file_1)
    calc_md5(file_1)
    calc_md5sum(file_1)
    
    print ""
    print "Main program end."


