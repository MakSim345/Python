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

import os, sys
import urllib2
import time
import zlib
from search_and_destroy import *
from search_dublicates import search_dublicates
from file_manager import md5_hash
from file_manager import file_manager
from sms_rus import sendSMS
from log_engine import *

# main entrance point:
if __name__ == "__main__":
    # print u"Программа началась."
    print ""
    
    # print "sys.path[0] = ", sys.path[0] 
    os.chdir(sys.path[0])
    
    _trace = logEngine()
    _trace.setLogFileName("log.log")
    _trace.saveToLog("init")
    _trace.saveToLog(sys.path[0])
    
    #predefined macros:
    NO_ERASE_FILES = False
    ERASE_FILES = True
    
    #check if it is linux:
    # search_path_main_box = "/home/yuriy/Dropbox/" 
    
    search_path_c_box = "C:/Dropbox"
    search_path_d_box = "D:/Dropbox"

    #select correct path to Win32 Dropbox:
    if os.path.exists(search_path_d_box):
        search_path_main_box = search_path_d_box
    if os.path.exists(search_path_c_box):
        search_path_main_box = search_path_c_box
    #   sys.stderr.write("Info: '"+self.filename+"' does not exist. Nothing to do\n")    
    #else:        
    #    sys.stderr.write("Info: '"+self.filename+"' does exist.\n")
    # endif 
    
    print "Dropbox path: ", search_path_main_box 
    _sd = search_dublicates(search_path_main_box)
    _sd.run(NO_ERASE_FILES)
    _result_to_send = _sd.compare_dictionaryes()

    sender =  sendSMS('YANDEX', 'dropbox')
    result = sender.send_info_sms(_result_to_send)
    
    print ""
    print "Main program end."
