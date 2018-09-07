#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

# ============================================================
#
#
# ============================================================
#
#
# Author:         YS /
#
# ============================================================
# ============================================================

import os, string
import urllib2
import time
import shutil
import pickle
from datetime import date

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0
        self.status = 0

class logEngine(): 
    
    def __init__(self):
        self._log_file_name = 'log_run_copy.log'

    def saveToLog(self, _text):        
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("TRACE:\n")
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

class find_and_move(): 
    
    def __init__(self, dir_src, dir_dst, file_extend):
        self._log = logEngine()
        self._dir_src = dir_src
        self._dir_dst = dir_dst
        self._file_extend = file_extend

    def run(self):
        selected_files = []
        for root, subFolders, files in os.walk(self._dir_src):
            for file in files:
                print file
                filePath = self._dir_src + '/' + file
                ext = string.split(file, '.')
                if  self._file_extend in ext:
                    _str_log =  "Move file " + filePath
                    print _str_log
                    self._log.saveToLog(_str_log)
                    selected_files.append(filePath)
                    shutil.move(filePath, self._dir_dst)
                    break
                #endif
            #end for
        #end for
        print selected_files# filePath

def power_off():
    import subprocess
    subprocess.call(["shutdown.exe", "-f", "-s", "-t", "60"])

def save_status(data_to_save, dat_file_name):
    pickle.dump(data_to_save, open(dat_file_name, "wb"))

def read_status(dat_file_name):
        if not os.path.exists(dat_file_name):
            _err_msg = "ERROR: File " + self._dat_file_name + " does not exists!"
            print _err_msg
            # self.log.saveMessageToLog(_err_msg)
            return
        #endif 
    
        data_to_save = pickle.load(open(dat_file_name, "rb"))
        return data_to_save

def tmp_():
    dat_file_name = "D:/tdata_str.dat"
    status = {"none":0, "first":1, "second":2, "last":3, "over":100}
    str_current_date = str(date.today())
    nd = net_data()
    nd.date = str(date.today())
    nd.total = 89.81
    nd.status = status.get("last")
    
    save_status(nd, dat_file_name)

    nd2 = read_status(dat_file_name)
    _tmp_date = str(nd2.date)
    _tmp_traff =  str(nd2.total)
    _tmp_status = str(nd2.status)
    #self.log.saveMessageToLog("3a cyTku " + _tmp_date + ": " + _tmp_traff + " MB.")
    print "3a cyTku " + _tmp_date + ": " + _tmp_traff + " MB."
    print "CTaTus: ", _tmp_status
    if (_tmp_date == str_current_date):
         print "CyTku coBnaLu!"
    #endif

# main entrance point:
if __name__ == "__main__":
    print ""
    
    # make sure that these directories exist
    dir_src = "d:/tmp"
    dir_dst = "d:/"  

    _sd = find_and_move(dir_src, dir_dst, "rar")
    _sd.run()
    # power_off()


    print ""
    print "Main program end."
