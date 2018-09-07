#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import traceback  

#############################################################################
##
##
#############################################################################

import math
number = 5

# coding:utf8

import time
from datetime import datetime, timedelta

'Получить текущее время и дату'
print datetime.now()
#> 2010-08-14 02:58:15.057495

d = datetime.today()
print d
#> 2010-08-14 02:58:15.057538

'Форматированный вывод'
print d.strftime('%y-%m-%d %H:%M:%S')
#> 10-08-14 02:58:15

'Сдвинуть время'
print d + timedelta(days=1, hours=1)
#> 2010-08-15 03:58:15.057538

'Конвертировать время POSIX в datetime'
print datetime.fromtimestamp(time.time())
#> 2010-08-14 02:58:15.057613

'Изменить атрибут'
print d.replace(year=2011,hour=11)
#> 2011-08-14 11:58:15.057538
#replace(year, month, day, hour, minute, second, microsecond, tzinfo)

'Получить кортеж'
print d.timetuple()
#> time.struct_time(tm_year=2010, tm_mon=8, tm_mday=14, tm_hour=2,
#> tm_min=58, tm_sec=15, tm_wday=5, tm_yday=226, tm_isdst=-1)

'Получиь день недели, 0 - Пн, 6 - Вс'
print d.weekday()
#> 5

'Получить дату'
print d.date()
#> 2010-08-14

'Получить время'
print d.timetz()
#> 02:58:15.057538

'Сложить дату и время'
print d.combine(d.date(),d.timetz())
#> 2010-08-14 02:58:15.057538

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
    print "\nTiming a 1 million loop 'for loop' ..."
    start = time.clock()
    for x in range(1000000):
        y = 100*x - 99 # do something
    end = time.clock()
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
    print sys.getcheckinterval()
    for i in range (100):
         # now = time.time()
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now
    print 'STOP'

def TimeTest003():
    import time
    import sys
    import arrays

    for i in range (10):
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now, "QT: ", m_ms.elapsed()

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
    
def someInt():
    return 690    

def someFloat():
    return 23.45
    
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


print "Main program begins"
#f3()
#print 'function returns: ', ReturningVals()
#for i in range(10):
#    print i*2
#SaveStatus (MyArray())
#test003("3")
MyTuple()
    
print "Main program ends"

#D = 'test'
#print "Before function call D = ", D
#printRoots(1.0, 0, -1.0)
#print "After function call D = ", D

#printMyNum()


'''import pickle, time, sys

mydata = ("abc", 12, [1, 2, 3])
output_file = open("mydata.dat", "w")
p = pickle.Pickler(output_file)
p.dump(mydata)
output_file.close()
'''
