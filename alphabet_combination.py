#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import time
import string


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

def _list_of_2_letter_combinations():
    ''' test function'''
    _dict = {}
    array = []
    counter = 0
    a = string.letters[:26]
    for letter in a:
        # print letter
        for sub_letter in a:
            _tmp_res = letter + sub_letter
            # _dict[_tmp_res] = counter
            if _tmp_res in array:
                print "Doublicate:", _tmp_res
            else:    
                array.append(_tmp_res)
                counter = counter+1
        #endif       
    #endif
    print counter
    print array
    # print _dict
    
if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        _list_of_2_letter_combinations()
        
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    

    print "\n----------------------"
    print "Main program ends"
