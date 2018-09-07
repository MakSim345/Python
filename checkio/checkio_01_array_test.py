import os
import sys

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0


def checkio_(els):
    a = 0
    for i in range(3):#(len(els)):
        a = a + els[i]
        # print a
        # i = i + i
    # print "return value:", a
    return a

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list
def my_checkio(els):
    a = [] # new array
    comm_arr = [] # new array
    ret_arr = [] # new array
    for b in els:
        if b in a:
            comm_arr.append(b)
        else:
            a.append(b)
    # print "array a: ", a
    for c in els:
        if c in comm_arr:
            ret_arr.append(c)
        else:
            pass
    print "ret_arr: ", ret_arr
    return ret_arr

def checkio(els):
    return [i for i in els if els.count(i) > 1]

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    #number = input ("Enter a non-negative integer to take factorial of: ")
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"


    print ""
    print "Main program end."
