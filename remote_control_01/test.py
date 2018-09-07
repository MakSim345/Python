#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import os
import time
import sys, traceback
from datetime import date

# from send_sms_traffic_warning import sendSMS

#from logger import logEngine
import pickle
import urllib2

class test():    
    def __init__(self):
        self.filename = 'run'
        self._action()
        self._is_log = False

    def _action(self):
        d = {}
        # fp = open(self.filename, self.rmode)
        fp = open(self.filename)
        for line in fp:
            # print line 
            items = line.split()
            # (key, val) = line.split()
            key, val = items[0], items[1:]
            print "key:", key, "val:", val
            d[key] = val
            
        #end_for
        #print d
        if 'echo' in d:
            print "echo is in d and =", d['echo']
            # print type(d['echo'].pop())
            if d['echo'].pop() == 'off':
                print "Echo OFF"
                self._is_log = False
            else:
                print "Echo ON"
                self._is_log = True
    #end_def    
        
    def action(self):
        ''' read file, run all commands from it and erase file.'''
        self._is_log = True
        fp = open(self.filename, self.rmode)
        
        lines = fp.readlines()
        for line in lines:
            # print line
            exec_line = self.make_exe_line(line)
            print exec_line
            os.system(exec_line)
            time.sleep(1)
        #endif   
    
        #for line in fp:
        #    print(line)  
        fp.close()
        self.remove_file(self.filename)
    #end def 

    def remove_file(self, _file_to_remove):
        ''' Remove the file '''
        if os.path.exists(_file_to_remove):
            # os.remove(_file_to_remove)
            print "File " + _file_to_remove + " deleted succesfully! - OK\n"
    #end def

    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    # log = logEngine()
    # log.saveMessageToLog("init OK.")
    rm_ctr = test()
    # rm_ctr.run()

    #endif 
    print ""    
    print "Main program end."

