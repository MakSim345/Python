#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import traceback  
import threading
import math
import time
import multiprocessing
import string
import random
from datetime import datetime, timedelta

def writer(_to_print, event_for_wait, event_for_set):
    for i in xrange(10):
        event_for_wait.wait() # wait for event
        event_for_wait.clear() # clean event for future
        print _to_print
        event_for_set.set() # set event for neighbor thread
    #end for
#end_def   

def TimeFunction():
    return time.time()
    # print time.mktime()

def writer2(filename, n):
    with open(filename, 'w') as file_out:
        for i in range (n):
            print >> file_out, i
        #end_for    
#end_def  

def test_foo_3():
    a = TimeFunction()
    print a
    
    t1 = threading.Thread(target=writer2, args=('test2.txt', 500000,))
    t2 = threading.Thread(target=writer2, args=('test3.txt', 500000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    b = TimeFunction()
    print b
    print "Diff:", b - a
#end_def

def password_generator(y):
    f = list(string.ascii_letters+string.digits)
    # print f
    _result = ''
    _result2 = ""
    for i in range(y):
        a = random.randint(0, len(f) - 1)
        # print a, 
        b = f[a]
        # print b,
        #_result.join(b)
        _result = _result + b
        # print "_result", _result
    return _result        

def start_calculation():
    for i in range(13107300):
        f_name =  password_generator(15) 
        f_name = f_name  + '.log'
        file_out = open(f_name, 'w+')
        print >> file_out, password_generator(150)  
        file_out.close

        if i % 10000 == 0:
            print i        
    #end_for
    

if __name__ == "__main__":
    print "--------------Main program begins---------------"
    print ""
    a = TimeFunction()
    #test_foo_3()
    print "ATTENTION! this will create a lot of files with random names and hang your system!"
    if raw_input("Are you sure you want to continue! ") not in ['y','Y']:
       print "Cancelled!"
    else:
       print "main calculation routine is commented!"
       # start_calculation()

    b = TimeFunction()
    print b
    print "Time Diff:", b - a
    print ""    
    print "--------------Main program ends-----------------"
