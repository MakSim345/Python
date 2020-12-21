#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
import sys, os
import time
import smtplib
import traceback

class logEngine():
    def __init__(self):
        self._name_of_file = 'modem_reset.log'
        self._log_file_path = '.'

    def saveMessageToLog(self, _text):
        #file = open(self._log_file_name, "a")
        file = open(os.path.join(self._log_file_path,  self._name_of_file), "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

class process_kill():
    def __init__(self):
        '''- '''
        self.array_to_terminate = []

    def set_ge_process_list(self):
        GENotify = "GENotify.exe"
        Windows10Upgrade = "Windows10Upgrade.exe"
        self.array_to_terminate.append(GENotify)
        self.array_to_terminate.append(Windows10Upgrade)

    def set_list_to_terminate(self, _array):
        self.array_to_terminate = _array
    #endif

    def kill_process(self, _process_to_kill):
        # os.system("taskkill /im Genied.exe /f")
        # print "\nProcess " + _process_to_kill + " will be terminated!"
        exec_line =  "taskkill /im " + _process_to_kill +" /f"
        os.system(exec_line)
    #endif

    def kill_all_processes(self):
        ''' kills all processes from the internal array'''
        for key in self.array_to_terminate:
            # print (key)
            self.kill_process(key)
        #end_for
    #endif

    def kill_all_ge_processes(self):
        self.set_ge_process_list()
        self.kill_all_processes()
    #endif



# main entrance point:
if __name__ == "__main__":

    print("Main program begins")

    pk = process_kill()
    pk.kill_all_ge_processes()
    # pk.kill_process("GENotify.exe")
    # pk.kill_process("Windows10Upgrade.exe")
    # subprocess.call(["C:/Program Files/VistaSwitcher/vswitch64.exe"])
    # subprocess.Popen(["C:/Program Files/VistaSwitcher/vswitch64.exe"])

    print("Main program ends")
