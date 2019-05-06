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
import platform
import sys

def cls():
    from subprocess import call
    from platform import system

    os = system()
    if os == 'Linux':
        call('clear', shell = True)
        print "OS - Linux"
    elif os == 'Windows':
        call('cls', shell = True)
        print "OS - Windows"

# main entrance point:
if __name__ == "__main__":
    print ""
    
    cls()

    # print "current platform is running under: ", platform.platform()
    print "Current platform is running under:", platform.system()
    print "Release: ", platform.release()
    print sys.platform
    print os.name

    if (os.name == "posix"):
        print os.system("uname -a")
    # insert other possible OSes here
        # ...
    else:
        print "--unknown OS, possible Windows"
    

    print "Main program end."
