#!/usr/bin/python
# Observer01.py

import threading, os, sys
import sys, traceback
import time

theVar = 1

class MyArray():

    def __init__(self):
        self.__privateVar = 23
        self.a = []
        for i in range(10001):
            self.a.append(i)

    def printMe(self):
        print self.a
    
    def showPrivate(self):
        print self.__privateVar

class timeKiller(threading.Thread):
    def __init__(self, timeToKill = 3):
        global theVar
        self.retKill = False
        self.timeToKill = timeToKill
        threading.Thread.__init__(self)
        print 'This is KILLER thread ' + str(theVar) + ' speaking.'
        theVar = theVar + 1

    def run(self):        
        self.t1 = time.clock()
        while 1:
            self.t2 = time.clock()
            time.sleep(0.1)
            self.k = int(self.t2 - self.t1)
            #print self.t2 , 'KILLER thread. k = ', self.k    
            if self.k > self.timeToKill:
                self.retKill = True
                break
        print 'KILLER thread done!!! Now kill others....'
        print "self.retVal() returns: ", self.retVal()

    def retVal(self):
        return  self.retKill

class busyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global theVar
        self.__goOn = True
        self.myName = str(theVar)
        theVar = theVar + 1
        print 'This is thread ', self.myName, ' speaking.'        

    def run(self):
        while self.__goOn:
            self.do_something()
            #self.myclass.critical_function()
        #print 'Thread ', self.myName, ' completed!'
    
    def setON(self, n=True):
        self.__goOn = n
        print 'setON: __goOn set to ', self.__goOn

    def kill (self):
        self.setON(False)

    #dummy function for load a CPU
    def do_something(self):
        pass

class MyThread(threading.Thread):
    def run(self):
        global theVar
        #print 'This is thread ' + str(theVar) + ' speaking.'
        print str(theVar)
        #print 'Hello and good bye.'
        theVar = theVar + 1    
        # self.myclass = MyClass()
        #while 1:
        #    do_something()
        #    self.myclass.critical_function()
            
class MyError002(Exception):
    def __init__(self):
        print 'MyError002 occures! Damn you.'           


class TalentAgency():
    def __init__(self, n = 0):
        self.ourActors = []
        
    def registerActor(self, argActor, argDesiredTypeOfRole):
        observer = Observer()
        observer.actor = argActor
        observer.desiredRole = argDesiredTypeOfRole
        self.ourActors.append(observer)
    
    def notify(self, castingCall):
        self.notifyActors(castingCall)

    def notifyActors(self, castingCall):
        for observer in self.ourActors:
            if observer.desiredRole == castingCall.role:
                print observer.actor, ' got call for: ', castingCall.role

class CastingCall():
    def __init__(self):
        self.source = 'none'
        self.role = 'none'

class Observer():
    def __init__(self):
        self.actor = 'none'
        self.desiredRole = 'none'


if __name__ == "__main__":
    print "Main program begins"
    print ""
    try:
        HotShots = TalentAgency()
        HotShots.registerActor("Larry", "male lead")
        HotShots.registerActor("Moe", "male lead")
        HotShots.registerActor("Curly", "comic sidekick")
        
        castingCall = CastingCall()
        castingCall.source = 'Universal Studio'
        #castingCall.role = 'male lead'
        castingCall.role = 'comic sidekick'

        HotShots.notify(castingCall)

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
        


