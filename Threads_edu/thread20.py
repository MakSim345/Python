#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
import threading
import math
import time
import multiprocessing
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
            print >> file_out, i,
        #end_for
#end_def

def test_foo_1():
    a = TimeFunction()
    print a
    writer2("new_file.txt", 1000000)
    b = TimeFunction()
    print b
    print "Diff:", b - a
#end_def

def test_foo_2():
    # init events
    e1 = threading.Event()
    e2 = threading.Event()

    # init threads
    t1 = threading.Thread(target=writer, args=(0, e1, e2))
    t2 = threading.Thread(target=writer, args=(1, e2, e1))

    # start threads
    t1.start()
    t2.start()

    e1.set() # initiate the first event

    # join threads to the main thread
    t1.join()
    t2.join()
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

def test_foo_4():
    worker_count = multiprocessing.cpu_count()
    print "PS has", worker_count, "processors"
    jobs = []
    for i in xrange(worker_count):
        _file_name = 'new_file_' + str(i) + '.txt'
        p = multiprocessing.Process(target = writer2, args=(_file_name, 5000000))
        jobs.append(p)
        p.start()
    #end_for
    for w in jobs:
        w.join()
#end_def


if __name__ == "__main__":
    print "--------------Main program begins---------------"
    print ""

    test_foo_4()

    print ""
    print "--------------Main program ends-----------------"

