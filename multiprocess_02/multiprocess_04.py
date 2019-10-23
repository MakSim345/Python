#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import datetime
import threading
import logging
import multiprocessing

class FakeDatabase(object):
    """docstring for FakeDatabase"""
    def __init__(self):        
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

def thread_function(nameP): 
    ''' thread starts'''
    logging.info("Thread %s: starting", nameP)
    time.sleep(2)
    logging.info("Thread %s: finishing", nameP)

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= number
    return fact    

def setConfig():
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

def testOne():
    logging.info("Main      : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    
    logging.info("Main      : before running thread")
    x.start()

    logging.info("Main      : wait for the thread to finish")
    x.join()

    logging.info("Main      : all done")

def testTwo():
    threads = list()
    for index in range(3):
        logging.info("Main      : create and start thread %d", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

def thread_run(numberOfThreads): 
    ''' thread '''
    threads = list()
    number = 100000
    startTime = time.time()
    for index in range(numberOfThreads):
        logging.info("Main:    create and start thread %d", index)
        new_thread = threading.Thread(target=factorial, args=(number,))
        threads.append(new_thread)

    for i in range(numberOfThreads):
        threads[i].start()
        threads[i].join()
    
    endTime = time.time()
    print "Threads: factorial process took", endTime - startTime

def thread_run_simple(): 
    ''' test threads in simple way '''
    number = 100000
    startTime = time.time()    
    
    logging.info("Main:    create and start thread 1")
    t1 = threading.Thread(target=factorial, args=(number,))
    t1.start()

    logging.info("Main:    create and start thread 2")
    t2 = threading.Thread(target=factorial, args=(number,))
    t2.start()

    logging.info("Main:    create and start thread 3")
    t3 = threading.Thread(target=factorial, args=(number,))
    t3.start()

    t1.join(); t2.join(); t3.join()
    
    endTime = time.time()
    print "Threads: factorial process took", endTime - startTime    

def process_run_simple(): 
    ''' test processes in simple way '''
    number = 100000
    startTime = time.time()
    
    logging.info("Main:    create and start process 1")
    p1 = multiprocessing.Process(target=factorial, args=(number,))
    p1.start()

    logging.info("Main:    create and start process 2")
    p2 = multiprocessing.Process(target=factorial, args=(number,))
    p2.start()

    logging.info("Main:    create and start process 3")
    p3 = multiprocessing.Process(target=factorial, args=(number,))
    p3.start()

    p1.join(); p2.join(); p3.join()
        
    endTime = time.time()
    print "Process: factorial process took", endTime - startTime

def process_run(numberOfProcesses): 
    ''' process '''
    processes = list()
    number = 100000
    startTime = time.time()
    for index in range(numberOfProcesses):
        logging.info("Main:    create and start process %d", index)
        new_process = multiprocessing.Process(target=factorial, args=(number,))
        processes.append(new_process)
    
    for i in range(numberOfProcesses):
        processes[i].start()
        processes[i].join()

    endTime = time.time()
    print "Process: factorial process took", endTime - startTime

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    setConfig()
    
    logging.info("CPU count: %d", multiprocessing.cpu_count())
    
    divg = 3
    # thread_factorial = threading.Thread(target=factorial, args=(number,))
    
    thread_run(divg)
    process_run(divg)
    
    thread_run_simple()
    process_run_simple()

    # testOne()
    #database = FakeDatabase()
    #logging.info("Testing update. Starting value is %d", database.value)


    print "==============================================================="
    print "Main program ends"
