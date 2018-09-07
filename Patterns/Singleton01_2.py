#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading, os, sys
import sys, traceback
import time

class Singleton(object):
    _instance = None
    def __new__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance


class Singleton_2(object):
    _instance = {}
    def __new__(self, id):
        try:
            return self._instance[id]
        except:
            d = super(Singleton, self).__new__(self) 
            self._instance[id] = d
            return d

# main entrance point:
if __name__ == "__main__":

    print "Main program begins"
    print ""
    
    a=Singleton()
    b=Singleton()
    print id(a), id(b)
    
    print ""
    print "Main program ends"


