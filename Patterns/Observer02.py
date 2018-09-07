#!/usr/bin/python
# Observer02.py
import threading, os, sys
import sys, traceback
import time
           
class MyError002(Exception):
    def __init__(self):
        print 'MyError002 occures! Damn you.'           

def demoHandler(argEvent):
    print "Handling", argEvent.type, "from", argEvent.source

class CastingCall():
    def __init__(self):
        self.source = 'none'
        self.role = 'none'

class Event():
    def __init__(self):
        self.type = 'none'
        self.source = 'none'

class Observer():
    def __init__(self):
        self.eventType = 'none'
        self.eventHandler = 'none'

class Dispatcher():
    def __init__(self, n = 0):
        self.myObservers = []
        
    def registerObserver(self, argEventHandler, argEventType):
        observer = Observer()
        observer.eventHandler = argEventHandler
        observer.eventType = argEventType
        self.myObservers.append(observer)
    
    def eventArrival(self, argEvent):
        self.notifyObservers(argEvent)
    
    def printMyObservers(self):
        print 'printMyObservers: '
        for i in self.myObservers:
            print i.eventType , i.eventHandler

    def notifyObservers(self, argEvent):
        for observer in self.myObservers:
            if observer.eventType == argEvent.type:
                observer.eventHandler(argEvent)

if __name__ == "__main__":
    print "Main program begins"
    print ""
    try:
        demoDispatcher = Dispatcher()
        demoDispatcher.printMyObservers()
        
        MOUSE_LEFT_DOUBLE = "LeftMouseDoubleClick"

        demoDispatcher.registerObserver(demoHandler, MOUSE_LEFT_DOUBLE)
        
        demoEvent = Event()
        demoEvent.type = MOUSE_LEFT_DOUBLE
        demoEvent.source = 'mouse'

        demoDispatcher.eventArrival(demoEvent)
        demoDispatcher.printMyObservers()

    except NotImplementedError, e:
        print "1. NotImplementedError occures:",  e
        #traceback.print_exc()
    except AttributeError, e:
        print "2. AttributeError occures:",  e
        #traceback.print_exc()
    except MyError002, e:
        print "3. MyError002 occures:", e
        #traceback.print_exc()
    except:
        print "4. Unknown error occures:"
        traceback.print_exc()    

    print ""    
    print "Main program ends"

