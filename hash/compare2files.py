#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date
import hashlib
from time import time

# reload(sys)
# sys.setdefaultencoding('utf-8')

import locale

def md5 (fname):
    md5hash = hashlib.md5()
    with open (fname) as file_handle: # open the file one line at a time, save memory
        for line_in_file in file_handle:
            # md5hash.update(line_in_file.encode('utf-8')) 
            md5hash.update(line_in_file) 
            # md5hash.update(line_in_file.decode('utf-8')) 
    return md5hash.hexdigest()

def sha1 (fname):
    sha1hash = hashlib.sha1()
    with open (fname) as file_handle: # open the file one line at a time, save memory
        for line_in_file in file_handle:
            sha1hash.update(line_in_file) 
            # sha1hash.update(line_in_file.encode('utf-8')) 
            # sha1hash.update(line_in_file.decode('utf-8')) 
    return sha1hash.hexdigest()    
    
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
    files = [ sys.argv[1], sys.argv[2] ] # these are the arguments we take
    
    # print locale.getpreferredencoding(False)
    start_time = time()
    
    a = md5(files[0])    
    b = md5(files[1])
    
    if a == b:
        print('MD5: Matched')
    else:
        print('MD5: Not Matched')

    end_time = round (time() - start_time, 3)
    print a
    print b
    print ("Calculation took " + str(end_time) + "ms\n")
    
    start_time = time()
    a = sha1(files[0])    
    b = sha1(files[1])
   
    if a == b:
        print('SHA1: Matched')
    else:
        print('SHA1: Not Matched')

    end_time = round (time() - start_time, 3)
    print a
    print b
    print ("Calculation took " + str(end_time) + "ms\n")

    print ""
    print "Main program end."