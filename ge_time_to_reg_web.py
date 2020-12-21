#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# ============================================================
#
# APR-2015.
# YS. 
# Script for create a string with current date minus 30 days 
# for RegWeb
# The result string shall be in the Clipboard, use Ctrl+V.
# ============================================================

import string
import sys
import time
import win32clipboard # pip install pywin32
from datetime import datetime, timedelta

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

if __name__ == "__main__":
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    d = datetime.today()
    print (d)

    #shift date:
    dd = d + timedelta(days=-30)
    print (dd)
    
    start_date = dd.strftime('%d.%m.%y')
    end_date = d.strftime('%d.%m.%y')
    s = "http://regweb.euro.med.ge.com/report.asp?tid=1&sdate={}&edate={}&sb-show=Show"
    s = s.format(start_date, end_date)
    print (s)
    copy(s)
    print ("Now paste and observe")
    


