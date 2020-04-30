#!/usr/bin/python
# ============================================================
#
#
# ============================================================
#
# Project:        
#
# Author:         YS
#
# ============================================================
# 
# ============================================================
import os
import time

class logEngine():

    def __init__(self):
        self.setLogFileName('check_dropbox.log')

    def setLogFileName(self, _file_name):
        self._log_file_name = _file_name

    def saveToLog(self, _text):
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("RESULT:\n")
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()
