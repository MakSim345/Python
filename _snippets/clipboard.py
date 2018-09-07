#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================
#
# ============================================================
# ============================================================

import os
import sys
import platform
import win32clipboard
from datetime import datetime, timedelta

def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data


# main entrance point:
if __name__ == "__main__":
    
    d = datetime.today()
    print d
    #> 2010-08-14 02:58:15.057538
    text = d.strftime('%y-%m-%d %H:%M:%S')
    print "copy to clipboard: today date:", text
    copy(text)
    print "Now paste and observe"
    print "\nMain program end."



