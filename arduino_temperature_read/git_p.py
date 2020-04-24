#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date
import datetime


# main entrance point:
if __name__ == "__main__":
    print "Main program start"
    
    str_path_on_os = '/home/ys/web_tmp'
    os.chdir(str_path_on_os)
    # push to bitbucket
    os.system('python commit_me.py')
        
    #os.system("git add .")
    #os.system("git commit -m 'update temperature'")
    #os.system("git push")

    print "Main program end."
