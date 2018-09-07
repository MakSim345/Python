#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import string
import os
import time
import sys, traceback
from datetime import date

# from send_sms_traffic_warning import sendSMS

from logger import logEngine
import pickle
import urllib2

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0

class serial_controller():
    def __init__(self):
        ''' init'''
        self.port_name = '/dev/ttyACM0'
        # self.port_name = 'COM2'

    def open_port(self):
        try:
            self.ser = serial.Serial(self.port_name, 9600)
        except serial.SerialException:
            print "ERROR in open port", self.port_name

    def write_to_port(self, _to_port = 'A'):
        self.ser.write(_to_port)

    def close_port(self):
        self.ser.close()

    def recv(self):
        return self.port.readline()

class net_control():
    def __init__(self, _silent_mode = False):
        '''init'''
        self._silent_mode = _silent_mode

    def __exit__(self):
        self.log.saveMessageToLog("END.")

    def save_status(self, data_to_save):
        pickle.dump(data_to_save, open(self._dat_file_name, "wb"))

    def read_status(self):
        self.get_initial()

        if not os.path.exists(self._dat_file_name):
            _err_msg = "ERROR: File " + self._dat_file_name + " does not exists!"
            # print _err_msg
            self.log.saveMessageToLog(_err_msg)
            return
        #endif

        nd2 = pickle.load(open(self._dat_file_name, "rb"))

        _tmp_date = str(nd2.date)
        _tmp_traff = r"%3.2f" % (nd2.total)
        _tmp_status = nd2.status

        self._start_message = str(_tmp_date) + " Траффик: " + str(_tmp_traff) + " MB. "
        # self.log.saveMessageToLog("3a cyTku " + _tmp_date + ": " + _tmp_traff + " MB.")

        if (_tmp_date == self._str_current_date):
            self.bytes_rec_init = self.bytes_rec_init - float(_tmp_traff)
            self._current_status = _tmp_status
        #endif

    def reset_status(self):
        self._current_status = self.status.get("none")

    def set_date(self):
        self._str_current_date = self.get_current_date()

    def get_current_date(self):
        return str(date.today())

    def check_connection(self):
        '''Check an  internet connection'''
        try:
            response = urllib2.urlopen('http://google.com', timeout = 1)
            return True
        except urllib2.URLError as err: pass
        return False

    def if_internet(self):
        ''' test'''

    # main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""

    log = logEngine()
        # log.saveMessageToLog("Arduino modem control - init OK.")

    nc = net_control()
    ret = nc.check_connection()
    if (ret):
        print "Internet working - OK."
        # log.saveMessageToLog("Internet working - OK.")
    else:
        print "ERROR: Internet NOT working."
        #log.saveMessageToLog("ERROR: Internet NOT working.")
        serial_port = serial_controller()
        serial_port.open_port()
        serial_port.write_to_port()
        seral_port.close()
    #endif
    print ""
    print "Main program end."

