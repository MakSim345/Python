#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import string
import os
import time
import sys, traceback
from datetime import date
from random import random

def du_run():
    
    # basedir = "/home/user/test/"
    basedir = os.getcwd()

    subnames = os.listdir(basedir)
    
    for subname in subnames:
        sub_size = 0
        subpath = "%s\\%s" % (os.path.dirname(basedir), subname)
        
        # print "subpath = ", subpath

        # print "basedir = ", basedir
        # for path, subdirs, files in os.walk(subpath):
        for path, subdirs, files in os.walk(basedir):
            for file in files:                
                filename = os.path.join(path, file)
                # print "filename:", filename
                sub_size += os.path.getsize(filename) /1024 /1024
                # print sub_size,
            #end_for
            print "%s - %.1f Mb" % (basedir[len(basedir): ], sub_size)
        #end_for        
        
        # print "%s - %.1f Mb" % (basedir[len[basedir]: ], sub_size)
    #end_for    

def size_dir(d):
    file_walker = (
        os.path.join(root, f)
        for root, _, files in os.walk(d)
        for f in files
    )
    total_size = sum(os.path.getsize(f) for f in file_walker)
    ret_val = total_size /1024 /1024
    return ret_val

    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #number = input ("Enter a non-negative integer to take factorial of: ")
    #factorial_calc(number)

    #number = input ("Enter a non-negative integer: ")
    #print pi_calc_02(number)
    # print os.getcwd()

    # du_run()
    basedir = os.getcwd()
    print "%.1f Mb" % size_dir(basedir)

    print ""    
    print "Main program end."

