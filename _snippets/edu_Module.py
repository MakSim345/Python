import math
import time
import random

def Logariphm1():
    x = 1.0
    while x < 10.0:
        print x, "\t", math.log(x)
        x += 1.0

def Logariphm2():
    n = input("enter number: ")
    for n in range(1, 10):
        print n, "\t", math.log(n)

def PowerOfTwo():
    for n in range(101):
         print "2^", n, "\t", 2**n


def TimeFunction():
    print time.ctime()
    # print time.mktime()

class Stack:
    def __init__(self):
        """Stack init"""
        self._stack = []
    def top(self):
        """Top back"""
        return self._stack[-1]
    def pop(self):
        """Get top"""
        return self._stack.pop()
    def push(self, x):
        """Push"""
        self._stack.append(x)
    def __len__(self):
        """Amount"""
        return len(self._stack)
    def __str__(self):
        """stack As A String"""
        return " : ".join(["%s" % e for e in self._stack])

def MyRandomFactory():
    for i in range(6):
        x = random.randint(1, 49)
        print x,

def AllcharactersPrint():
    for i in range(9000):
        print unichr(i),

    print '\n'

# Main application:
print "Main application starts:\n"
# Logariphm2()
#n = input("enter number: ")
#print n, "\t", math.log(n)
#PowerOfTwo()
# AllcharactersPrint()
currentTime()
TimeFunction()

print "\nMain application ends:"




