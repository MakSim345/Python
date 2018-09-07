#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import time
import urllib2
import sys, traceback
from net_control import net_control
from multithread_workers import workers


def checkConnection(): 
    '''Check an  internet connection'''
    try:
        response = urllib2.urlopen('http://google.com', timeout = 1)
        return True
    except urllib2.URLError as err: pass
    return False


# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""
    #silent_mode = False
    #traffic = workers(silent_mode)
    #traffic.run()
    print  checkConnection()

    print ""
    print "Main program ends"
