#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date
import datetime

# NOTES and REMARKS:

class month_str():
    def __init__(self):
        ''' init class'''
        STR_JAN="JAN"
        STR_FEB="FEB"
        STR_MAR="MAR"
        STR_APR="APR"
        STR_MAY="MAY"
        STR_JUN="JUN"
        STR_JUL="JUL"
        STR_AUG="AUG"
        STR_SEP="SEP"
        STR_OCT="OCT"
        STR_NOV="NOV"
        STR_DEC="DEC"
        self._month_str = {1:STR_JAN, 2:STR_FEB, 3:STR_MAR, 4:STR_APR,
                           5:STR_MAY, 6:STR_JUN, 7:STR_JUL, 8:STR_AUG,
                           9:STR_SEP, 10:STR_OCT, 11:STR_NOV, 12:STR_DEC}
    
    def get_month(self, month_int):
        '''return month in str'''
        return self._month_str.get(int(month_int))


# main entrance point:
if __name__ == "__main__":
    print ""

    mth_str = month_str() 
    _day = time.strftime("%d")
    _year = time.strftime("%Y")
    _month = time.strftime("%m")
        
    _date = "\n" + _day + '-' + mth_str.get_month(int(_month)) + '-' + _year
    _start_message = _date + "\nТекущее время - " + time.strftime("%H:%M:%S\n")
    print _start_message
    

    # uptime:
    elapsed = 1232121
    print "  Uptime:", datetime.timedelta(seconds=elapsed)

    print "Main program end."
