#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import urllib2
import time
import smtplib
import traceback

class logEngine(): 
    def __init__(self):
        self._name_of_file = 'modem_reset.log'
    	self._log_file_path = '/home/yuriy/Dropbox/[2] dev/Python/arduino_modem_reset/'

    def saveMessageToLog(self, _text):        
        #file = open(self._log_file_name, "a")
        file = open(os.path.join(self._log_file_path,  self._name_of_file), "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write(_text)
        file.write("\n-------------------------------------\n")
        file.close()

