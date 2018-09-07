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

# main entrance point:
if __name__ == "__main__":    

    print "Main program start."
    print ""

    # print "1/3 = ", 0%3
    try:
        a = mModel()
        #print a.mArray
        a.fillArray()
        
    except:
        traceback.print_exc()    
    
    print ""    
    print "Main program end."

