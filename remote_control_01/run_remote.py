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

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0

class remote_control():
    def __init__(self, _file_name = 'run'):
        '''init'''
        self._exit = False
        self._is_log = False
        self._max_iter = 1
        self.rmode = 'rb'
        self.filename = _file_name
    
    def Exit(self):
        print "App stop it's work!"
        self._exit = True

    def run(self):
        ''' main endless looop '''
        counter = 0
        while not self._exit:
            if not os.path.exists(self.filename):
                sys.stderr.write("Info: '"+self.filename+"' does not exist. Nothing to do\n")
                #sys.exit(1)
            else:
                self._action()
            # time.sleep(5)
            counter = counter + 1
            if counter >= self._max_iter:
                self.Exit()
        #end_while    
    
    def make_exe_line(self, _str_value):
        ''' REM: -2 is using to remove endline characters.'''
        if self._is_log:
            return _str_value[0:-2]  + " >> result.log"
        else:
            return _str_value[0:-2]
        #endif
    #end_def    

    def _action(self):
        ''' read file, run all commands from it and erase file.'''
        exec_line = ''
        self._is_log = True
        d = {}
        fp = open(self.filename, self.rmode)
        for line in fp:
            # (key, val) = line.split()
            items = line.split()
            key, val = items[0], items[1:]
            print "key:", key, "val:", val
            d[key] = val
            if key == 'echo':
                if val[0] == 'off':
                    print "ECHO OFF!:"
                    self._is_log = False
                if val[0] == 'on':
                    print "ECHO ON!:"
                    self._is_log = True
            elif key == 'REM':
                print "ignore follow line: ",line 
            else:
                exec_line = self.make_exe_line(line)
                print "This will be the exec line:"
                print exec_line
            #endif     
            os.system(exec_line)
            time.sleep(1)
        #end_for 
        fp.close()
        self.remove_file(self.filename)
        #print d
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
    rm_ctr = remote_control('run')
    rm_ctr.run()

    #endif 
    print ""    
    print "Main program end."

