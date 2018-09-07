#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
##
#############################################################################

import sys, os  
import traceback
import random


def main():
    a = []
    _dict = {'0':0}

    for x in xrange(1000):
        _tmp = int(random.random() * 1000)
        a.append(_tmp)
        if _tmp in _dict:
            _dict[_tmp] = _dict[_tmp] + 1
        else:
            _dict[_tmp] = 0
            
    print a

    for key in _dict:
        print key , " - ", _dict[key]


# main entrance point:
if __name__ == "__main__":        
    print "---START---"
    main()
    print "---END---"    

