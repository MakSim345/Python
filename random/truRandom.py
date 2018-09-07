#!/usr/bin/python
# MyClass.py
import math
import string
import os
import time

import urllib2
from sys import argv

# For GE internal network we have to use proxy:
# proxies = {'http': 'http://3.187.4.17:88'}
# proxies = {'http': 'http://3.187.157.236:9400'}
proxies = {'http': 'http://3.187.4.17:88'}
# proxies = {'http': 'http://gems.setpac.ge.com/pac.pac'} 
#os.environ['http_proxy'] = 'http://3.187.157.236:9400' 
os.environ['http_proxy'] = 'http://3.187.4.17:88' 
    

def take_true_random_number_48():
    true_rnd = "Try to get 48\n"
    #print true_rnd
    try:
        count = 1#int(argv[1])
        true_rnd = urllib2.urlopen("http://random.org/integers/?num=%d&min=1&max=48&col=1&base=10&format=plain&rnd=new" % count).read()
    except:
        print "ERROR in 48"
        #true_rnd = urllib2.urlopen("http://random.org/integers/?num=1&min=1&max=48&col=1&base=10&format=plain&rnd=new", proxies).read()

    #print true_rnd
    return true_rnd

def take_true_random_number_39():
    true_rnd = "Try to get 39\n"
    #print true_rnd
    try:
        count = 1# int(argv[1])
        true_rnd = urllib2.urlopen("http://random.org/integers/?num=%d&min=1&max=39&col=1&base=10&format=plain&rnd=new" % count).read()
    except:
        print "ERROR in function 'take_true_random_number_39()' "
        #true_rnd = urllib2.urlopen("http://random.org/integers/?num=1&min=1&max=39&col=1&base=10&format=plain&rnd=new", proxies=proxies).read()

    #print true_rnd
    return true_rnd

def take_true_random_number_bin():
    true_rnd = "Try to get bin\n"
    #print true_rnd
    try:
        count = 1# int(argv[1])
        true_rnd = urllib2.urlopen("http://random.org/integers/?num=%d&min=0&max=1&col=1&base=10&format=plain&rnd=new" % count).read()
    except:
        print "ERROR in 39"
        #true_rnd = urllib2.urlopen("http://random.org/integers/?num=1&min=1&max=39&col=1&base=10&format=plain&rnd=new", proxies=proxies).read()

    #print true_rnd
    return true_rnd


def lotto_seven():
    return lotto_7x39_number(7)

def lotto_six ():
    return lotto_6x48_number(6)

def lotto_6x48_number(number = 6):
    a = []
    for i in range(number):
        _origin = True
        while _origin:
            _tmp_number = int (take_true_random_number_48())
            #print _tmp_number
            if _tmp_number in a:
                #print "Incorrect:", _tmp_number, "is in array.", a
                _origin = True
            else:
                #print "Correct:", _tmp_number, "not in array.", a
                _origin = False
        a.append(_tmp_number)
        a.sort()
    return a
    
def lotto_7x39_number(number = 7):
    a = []
    for i in range(number):
        _origin = True
        while _origin:
            a = take_true_random_number_39()
            print a
            _tmp_number = int (a)
            #print _tmp_number
            if _tmp_number in a:
                #print "Incorrect:", _tmp_number, "is in array.", a
                _origin = True
            else:
                #print "Correct:", _tmp_number, "not in array.", a
                _origin = False
        a.append(_tmp_number)
        a.sort()
    return a

# main entrance point:
if __name__ == "__main__":    
    #print "Main program start."
    print ""
    #for i in range(10):
    # print take_true_random_number_bin()
    #take_true_random_number_48()
    for i in range(10):
        print lotto_seven()
    #print lotto_six()
    
    print "=================================="    
    #print "Main program end."
