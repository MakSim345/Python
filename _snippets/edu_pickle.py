#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
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

def StartPocess():
    argList = ("argument 1","argument 2","argument 3")
    mpathTotest = 'D:\dev\Python\test.exe'
    os.execvp(mpathTotest, ["argument 2"])
    #os.fork()

print "Main program begins"
#f3()
#print 'function returns: ', ReturningVals()
#for i in range(10):
#    print i*2
# CalcFibonacci()
# StartPocess()

#D = 'test'
#print "Before function call D = ", D
#printRoots(1.0, 0, -1.0)
#print "After function call D = ", D
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
#printMyNum()

def SaveStatus(data_to_save):
    import pickle, time, sys
    # mydata = ("abc", 12, [1, 2, 3])
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.dump(data_to_save)
    output_file.close()

def ReadStatus():
    import pickle, time, sys
    # data_to_save = []
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.get(data_to_save)
    output_file.close()

'''import pickle, time, sys

mydata = ("abc", 12, [1, 2, 3])
output_file = open("mydata.dat", "w")
p = pickle.Pickler(output_file)
p.dump(mydata)
output_file.close()
'''

if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        SaveStatus( MyArray() )
        print ReadStatus()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"



