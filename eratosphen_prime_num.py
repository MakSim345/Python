#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import time
import threading

def printRoots(a, b, c):
    D = b**2 - 4 * a * c
    print "In function D = ", D
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print "x1 =", x1, "\nx2 =", x2

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

def CalcFactorial():
    num = input("Enter a number for iteration: \n")
    print ("Factorial of %d is:" % num)
    print fact (num)

def CalcFibonacci():
    num = input("Enter a number for Fibo number: \n")
    print ("Fibonacci number %d is:" % num)
    print Fibonacci (num)

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

def EratosphenTimeTest(_function_as_param):
    # time.clock() gives wallclock seconds accurate to at least 1 millisecond
    # it updates every millisecond, but only works with windows
    # time.time() is more portable, but has quantization errors
    # since it only updates updates 18.2 times per second
    import time
    print "\nTiming a prime number calcuation:"
    start = time.clock()
    
    # worker = threading.Thread(target = Eratosphen_Prime_01, args = (10000,))
    worker = threading.Thread(target = _function_as_param, args = (10,))
    worker.start()
    worker.join()

    end = time.clock()    
    print 'start', start
    print 'end', end
    print "Time elapsed = ", end - start, "seconds"
    
def Eratosphen_Prime_01(_num):
    ''' simplest prime numbers calcuation functon'''
    if _num == 0:
        n = input("n=")
    else:    
        n = _num

    lst = []
    k = 0
    for i in xrange(2, n+1):
        for j in xrange(2, i):
            if i % j == 0:
                k = k+1
            #endif
        #endfor
        if k == 0:
            lst.append(i)
        else:
            k = 0    
    #endfor
    print lst          

def Eratosphen_Prime_02(_num):
    ''' advanced prime numbers calcuation functon'''
    if _num == 0:
        n = input("n=")
    else:    
        n = _num

    lst = []
    for i in xrange(2, n+1):
        for j in xrange(2, i):
            # print i, "%", j
            if i % j == 0:
                #print "- break"
                break
        else:
            #print "add to array"
            lst.append(i)
        #endfor
    #endfor
    print lst

def Eratosphen_Prime_03(_num):
    ''' ver 3: prime numbers calcuation functon'''
    if _num == 0:
        n = input("n=")
    else:    
        n = _num

    lst = []
    for i in xrange(2, n+1):
        # looking for dividers in ready-made prime numbers
        for j in lst:            
            if i % j == 0:
                #print "- break"
                break
        else: # strange operator, related to 'for j in lst:'
            #print "add to array"
            lst.append(i)
        #endfor
    #endfor
    print lst

def Eratosphen_Prime_04(_num):
    ''' ver 4: prime numbers calcuation functon
        dividers are no bigger than a sqrt of a number
    '''
    if _num == 0:
        n = input("n=")
    else:    
        n = _num

    lst = []
    for i in xrange(2, n+1):  
        print "For number ", i      
        for j in lst:
            print "--take: ", j
            if j > int(math.sqrt(i) +  1):
                print "--append: ", j, " is bigger than sqrt(", i, ") = ", int(math.sqrt(i))
                lst.append(i)
                break                                
            if (i % j == 0):
                print i ,"%", j, "= 0"
                break
        else: # strange operator, related to 'for j in lst:'
            #print "add to array"
            print "--append: ", i
            lst.append(i)
        #endfor
    #endfor
    print lst

if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        # a = [MyArray(), someInt(), someFloat()]
        #EratosphenTimeTest(Eratosphen_Prime_01)
        # EratosphenTimeTest(Eratosphen_Prime_02)
        # EratosphenTimeTest(Eratosphen_Prime_03)
        EratosphenTimeTest(Eratosphen_Prime_04)
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"
