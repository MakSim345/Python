#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import string
import os
import time
import sys, traceback
import psutil
from datetime import date
from send_sms_traffic_warning import sendSMS
from logger import logEngine
import pickle

class net_data():
    def __init__(self):
        '''init'''
        self.date = 0
        self.total = 0.0
        self.status = 0

class net_control():
    def __init__(self, _silent_mode = False):
        '''init'''
        self._silent_mode = _silent_mode
        self._counter = 0
        self.total = 0
        self.bytes_rec_init = 0
        
        self._limit = 232
        self._first_warning = 225
        self._last_warning = 230
        
        #self._limit = 23
        #self._first_warning = 15
        #self._last_warning = 20

        self._dat_file_name = "D:/trdata.dat"
        self._sent = False
        self.status = {"none":0, "first":1, "second":2, "last":3, "over":100}

        self.log = logEngine()
        self.log.saveMessageToLog("PEOPLENET (po6oT) - Ha4aLo pa6oTbI.")
        self.init_string_values()
        self.set_date()
        self.read_status()
        # self.get_initial()

    def init_string_values(self):
        self._str_attn_possible = r"BHuMaHue! y Bac CKOPO Bo3Mo*Ho npeBbIweHue LuMuTa uHTepHeT TpaFFuka. "
        self._str_attn_already  = r"Bce! KoMn OTkLI04eH - y Bac npeBbIweHue LuMuTa TpaFFuka! "
        self._str_attb_counter  = r"uHTepHeT TpaFFuk: %3.2f MB. "
        self._iRobot = "PEOPLENET (po6oT)."
    
    def __exit__(self):
        self.log.saveMessageToLog("PEOPLENET (po6oT) - 3aBepweHue pa6oTbI.")

    def save_status_default(self):
        nd = net_data()
        nd.date = self._str_current_date
        nd.total = self.total
        nd.status = self._current_status
    
        self.save_status(nd)

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
        self.log.saveMessageToLog("3a cyTku " + _tmp_date + ": " + _tmp_traff + " MB.")

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
    
    def date_check(self):
        ''' compare date and if day change, reset all rec/sent values'''
        _tmp_date = self.get_current_date()

        if not (_tmp_date == self._str_current_date):
            status = r"Last values. rec: %3.2f sent: %3.2f  Total: [%3.2f MB]" % (self.bytes_rec, self.bytes_sen, self.total)
            self.log.saveMessageToLog(status)

            _msg = "Date change from " + self._str_current_date + " to " + _tmp_date
            self.log.saveMessageToLog(_msg)
            if not self._silent_mode:
                print  _msg

            self.set_date()

            self.get_initial()
            self.get_current_traffic()

            status = r"New values. rec: %3.2f sent: %3.2f  Total: [%3.2f MB]" % (self.bytes_rec, self.bytes_sen, self.total)
            self.log.saveMessageToLog(status)
        #endif

    def get_initial(self):
        self.reset_status()
        self.ioc = psutil.network_io_counters()
        self.bytes_rec_init = self.ioc.bytes_recv/(1024*1024.0) + self.bytes_rec_init
        self.bytes_sen_init = self.ioc.bytes_sent/(1024*1024.0)

    def get_current_traffic(self):
        self.ioc = psutil.network_io_counters()
        self.bytes_rec = self.ioc.bytes_recv/(1024*1024.0) - self.bytes_rec_init
        self.bytes_sen = self.ioc.bytes_sent/(1024*1024.0) - self.bytes_sen_init
        self.total = self.bytes_rec + self.bytes_sen

    def run(self):
        while True:

            self.date_check()
            self.get_current_traffic()

            status = r"rec: %3.2f sent: %3.2f  Total: [%3.2f MB]" % (self.bytes_rec, self.bytes_sen, self.total)
            status = status + chr(8)*(len(status)+1)
            if not self._silent_mode:
                print status,
                # print status
            #endif

            self.check_limits()

            time.sleep(1)
            self._counter = self._counter + 1

            if self._counter == 30:
                self.save_status_default()
                # print _str
                self._counter = 0
            #endif

        #end while
    #end def

    def check_limits(self):
        '''A simple state machine implementation'''

        if (self._current_status == self.status.get("over")):
            return

        if (self._current_status == self.status.get("none")):
            if (int (self.total) > self._first_warning):
                _ATTN_ = (self._str_attb_counter + self._str_attn_possible) % (self.total)
                self.send_warning_sms(_ATTN_)
                self.save_status_default()
                self._current_status = self.status.get("first")
                return
            #endif
        #endif
        if (self._current_status == self.status.get("first")):
            if (int (self.total) > self._last_warning):
                _ATTN_ = (self._str_attb_counter + self._str_attn_possible) % (self.total)
                self.send_warning_sms(_ATTN_)
                self.save_status_default()
                self._current_status = self.status.get("last")
                return
            #endif
        #endif
        if (self._current_status == self.status.get("last")):
            if (int (self.total) > (self._limit + 5)):
                _ATTN_ = (self._str_attb_counter + self._str_attn_already) % (self.total)
                self.send_warning_sms(_ATTN_)
                self._current_status = self.status.get("over")
                self.save_status_default()
                self.power_off()
                #print "ATTN: POWER OFF!!! ------------------------------"
                return
            #endif
        #endif

    def power_off(self):
        import subprocess
        subprocess.call(["shutdown.exe", "-f", "-s", "-t", "60"])
    
    def send_warning_sms(self, _message = ""):
        try:
            sender =  sendSMS('YANDEX')
            _warning_message = _message + self._iRobot
            if not self._silent_mode:
                print _warning_message
            else:
                self.log.saveMessageToLog(_warning_message)
            #endif
            resultlt = sender.send_info_sms(_warning_message)

        except:
            traceback.print_exc()
            a ="ERROR: Failed sending SMS!"
            if not self._silent_mode:
                print a
            #endif
            self.log.saveMessageToLog(a)
            time.sleep(1)
    #end def

