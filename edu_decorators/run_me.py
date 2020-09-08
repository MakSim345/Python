import os, sys
import traceback
import time
import random

# ============================================================
class mModel():
    def __init__(self):
        self.mArray = range (1, 16)
        self.is_printed = False

    def mkRnd(self):
        return random.randint(1, 100)

    def dump(self):
        print self.mArray

    def fillArray(self):

        for i in self.mArray:
            self.is_printed = False
            # self.mArray.append(self.mkRnd())
            if not (i%3) and not (i%5):
                print i, "FuzzBuzz"
                self.is_printed = True

            if (not self.three_div(i)) and  not self.is_printed:
                self.is_printed = True
                print i, "Fuzz"

            if (not self.five_div(i)) and  not self.is_printed:
                self.is_printed = True
                print i, "Buzz"

            if not self.is_printed:
                print i

    def three_div (self, var):
        return var % 3

    def five_div (self, var):
        return var % 5
#=================================================================
# Decorators:

def a_stand_alone_function ():
    print "I'm a simple lonely function, you can not change me"

def my_shiny_new_decorator(a_function_to_decorate):
    """-"""
    def the_wrapper_around_the_original_function():
        print "Me - code run before function call"
        # call decorated functon:
        a_function_to_decorate()
        print "Me - code run after the function call"

    return the_wrapper_around_the_original_function


def doSomethingBefore(func):
    print "I'm doing something else before calling your function"
    print func()

def getTalk(type="shout"):
    # define functions here:
    def shout(word="yes"):
        print "inside shout"
        return word.capitalize()+"!"
    
    def whisper(word="yes"):
        print "inside whisper"
        return word.lower()+"..."

    print "before return: type=", type    
    if type == "shout":
        print "returning shout"
        return shout
    else:
        print "returning whisper"
        return whisper        

# main entrance point:
if __name__ == "__main__":

    print "Main program start."

    # print "1/3 = ", 0%3
    try:
        print "----------->"
        talk = getTalk()
        scream = getTalk()
        #print "talk is:", talk
        #print "talk() is:", talk()
        #print "talk('whisper') is:", talk("whisper")
        #print "getTalk('whisper') is:", getTalk("whisper")()
        # doSomethingBefore(scream)
        
        print "call a_stand_alone_function(): "
        a_stand_alone_function()
        a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
        a_stand_alone_function_decorated()
        print "The TRICK:----------->"
        a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
        print "call a_stand_alone_function(): "
        a_stand_alone_function()
    except:
        traceback.print_exc()

    print "Main program end."

