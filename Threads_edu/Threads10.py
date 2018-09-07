#!/usr/bin/env python
# ============================================================
#
# ============================================================
## Threads10.py - Threads in Python
## 
# ============================================================
import os, sys
import traceback
from PyQt4 import QtCore, QtGui
import thread
import threading
import time


def run_threadA (threadname, count, sleeptime):
  """This is the thread function to be invoked."""

  print "I am thread", threadname
  
  for i in range (1, count + 1):
      print "%s: count = %s" % (threadname, i)
      time.sleep(sleeptime)
    
  thread.interrupt_main()

def run_thread (threadname, sleeptime):
    """This is the thread function to be invoked."""

    global threadcount, activethreads

    print "%s: Current value of threadcount %s\n" % (threadname, threadcount)
    print "%s incrementing threadcount" % (threadname)
    threadcount = threadcount + 1
    time.sleep(sleeptime)  
    print "Value of threadcount after incremented by %s = %s" % (threadname, threadcount)
    activethreads = activethreads - 1
    print "%s exiting...." % (threadname)


if __name__ == "__main__":
    print "Main program begins"
    print ""
    
    threadcount=0
    activethreads = 4

    thread.start_new_thread(run_thread, ("Thread1", 1))
    thread.start_new_thread(run_thread, ("Thread2", 2))
    thread.start_new_thread(run_thread, ("Thread3", 3))
    thread.start_new_thread(run_thread, ("Thread4", 4))

    while activethreads > 0:
        pass 
    
    print ""    
    print "Main program ends"

