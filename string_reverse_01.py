#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import time

number = 5

def printMyNum():
    global number
    print number
    number = 3
    print number

def ReturningVals():
    a = 23+16
    b = 4+54
    return a, b

def printRoots(a, b, c):
    D = b**2 - 4 * a * c
    print "In function D = ", D
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print "x1 =", x1, "\nx2 =", x2

def f1():
    print "f1() begins"
    a = 1/2
    print "Hello world!", a
    print "f1() ends"

def fact(n):
    #print ("this is a %d iteration" % n)
    if n == 0:
        return 1
    return fact(n-1)*n

def Fibonacci(n):
    print ("iteration for: %d" % n)
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

def f2():
    print "f2() begins"
    f1()
    print "f2() ends"

def f3():
    print "f3() begins"
    f2()
    print "f3() ends"

def CalcFactorial():
    num = input("Enter a number for iteration: \n")
    print ("Factorial of %d is:" % num)
    print fact (num)

def CalcFibonacci():
    num = input("Enter a number for Fibo number: \n")
    print ("Fibonacci number %d is:" % num)
    print Fibonacci (num)

def setVentStatus(strVStatus):
    ventilationStatus = ("OFF", "ON", "PROCESSING", "OFF", "ON", "PROCESSING")
    VentStatus = ventilationStatus[2]
    print 'VentStatus(before) = ', VentStatus
    for i in ventilationStatus:
       if (strVStatus == i):
           VentStatus = i
    print 'VentStatus (after) = ', VentStatus

def TimeTest001():
    # time.clock() gives wallclock seconds accurate to at least 1 millisecond
    # it updates every millisecond, but only works with windows
    # time.time() is more portable, but has quantization errors
    # since it only updates updates 18.2 times per second
    import time
    a = []
    print "\nTiming a 1 million loop 'for loop' ..."
    start = time.clock()
    for x in range(1000000):
        y = 100*x - 99^99 # do something
        a.append(y) 
    end = time.clock()
    # print a
    print 'start', start
    print 'end', end
    print "Time elapsed = ", end - start, "seconds"
    """
    result -->
    Timing a 1 million loop 'for loop' ...
    Time elapsed = 0.471708415107 seconds
    """
def TimeTest002():
    import time
    import sys
    print "sys.getcheckinterval:", sys.getcheckinterval()
    for i in range (10):
         # now = time.time()
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now
    print 'STOP'

def SaveStatus(data_to_save):
    import pickle, time, sys
    # mydata = ("abc", 12, [1, 2, 3])
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.dump(data_to_save)
    output_file.close()

def ReadStatus():
    import pickle, time, sys
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.get(data_to_save)
    output_file.close()

def MyArray():
    a = [676.7, 353, 433, 14, 14.565]
    # a.sort()
    # print a
    return a
    
    
def MyTuple():
    a = [MyArray(), someInt(), someFloat()]
    # a = [66.6, 333, 333, 'Damn world', 1, 1234.5]
    # a.sort()
    for i in a:
        print i
    #return a
    
    
def dictTest():
    DeliveryStarted = 0
    DeliveryStopped = 1
    FGTotalFlowChanged = 2
    AgentTypeChanged = 3
    OxygenPercentageChanged = 4
    AirPercentageChanged = 5
    N2OPercentageChanged = 6
    AgentPercentageChanged = 7
    DummyAlarm = 8
    m_Array = {}  
    
    m_Array[DeliveryStarted]        = MyArray()
    m_Array[DeliveryStopped]        ="DeliveryStopped" 
    m_Array[FGTotalFlowChanged]     ="FGTotalFlowChanged" 
    m_Array[AgentTypeChanged]       ="AgentTypeChanged" 
    m_Array[OxygenPercentageChanged]="OxygenPercentageChanged" 
    m_Array[AirPercentageChanged]   ="AirPercentageChanged" 
    m_Array[N2OPercentageChanged]   ="N2OPercentageChanged" 
    m_Array[AgentPercentageChanged] ="AgentPercentageChanged" 
    m_Array[DummyAlarm]            ="DummyAlarm"
    
    if DeliveryStarted in m_Array:
        m_Array[0]

def _my_string_reverse(val_str = "abcdefgh"):
    ''' test function from an interview '''
    _string = val_str
    print _string
    _rev_string = ""
    str_len = len(_string)
    print "str_len=", str_len
    # q = _string.split()
    # print "string to array = ", q        
    for i in range(str_len):
        # _rev_string.append(_string[i])
        # print i
        _tmp = _string[(str_len-1) - i]
        # print _tmp
        _rev_string = _rev_string + _tmp
        # print q[i]
    #endfor    
    
    print _rev_string

if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        #f3()
        #print 'function returns: ', ReturningVals()
        #for i in range(10):
        #    print i*2
        #SaveStatus (MyArray())
        #test003("3")
        #D = 'test'
        #print "Before function call D = ", D
        #printRoots(1.0, 0, -1.0)
        #print "After function call D = ", D

        #printMyNum()
        # MyTuple()
        # TimeTest001()
        # _my_string_reverse("a po3a ynala Ha Lany azopa")
        _my_string_reverse()
        # a = lambda x: print x*x
        #print a(123)
        # a = [MyArray(), someInt(), someFloat()]
        
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"
