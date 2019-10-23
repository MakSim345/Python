#!/usr/bin/python
# ============================================================
#
# ============================================================

import urllib2
import time
from threading import Thread
import logging
import multiprocessing
from multiprocessing import Process


def set_config():
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO,
                        datefmt="%H%M%S")

class CountDownThread(Thread):
    def __init__(self, countP):
        Thread.__init__(self)
        self.m_count = countP

    def run(self):
        while self.m_count > 0:
            print "Counting down", self.m_count
            self.m_count -= 1
            time.sleep(2)
        return

def count(max_num):
    print "count start", max_num
    
    while max_num > 0:
        max_num -= 1
    #end_while

    print "count end", max_num

def usual_run():
    start_time = time.time()
    count(100000000)
    count(100000000)
    count(100000000)
    print "Usual count took", time.time() - start_time

def thread_run():
    start_time = time.time()
    t1 = Thread(target=count, args=(100000000,))
    t1.start()
    t2 = Thread(target=count, args=(100000000,))
    t2.start()
    t3 = Thread(target=count, args=(100000000,))
    t3.start()

    t1.join(); t2.join()
    print "Thread count took", time.time() - start_time

def process_run():
    start_time = time.time()
    t1 = Process(target=count, args=(100000000,))
    t1.start()
    t2 = Process(target=count, args=(100000000,))
    t2.start()
    t3 = Process(target=count, args=(100000000,))
    t3.start()

    t1.join(); t2.join()
    print "Process count took", time.time() - start_time


# main entrance point:
if __name__ == "__main__":

    set_config()
    logging.info("App start")
    logging.info("CPU count: %d", multiprocessing.cpu_count())
    usual_run()
    thread_run()
    process_run()
    logging.info("App END")

    print "Program ends"

