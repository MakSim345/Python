#!/usr/bin/python

import threading, os, sys
import sys, traceback
import smtplib  
import time
import string
import urllib2

class SendingThread(threading.Thread):

     def __init__(self, sender, message_to_send):
         self.sender = sender
         self._sms_to_send = message_to_send
        
    def set_sender(self, sender):
        self.sender = sender
        self._exit_thread = False
        self._sms_to_send = False
        self._msg_char = 0

    def check_connection(self): 
        '''Check an  internet connection'''
        try:
            response = urllib2.urlopen('http://google.com', timeout = 1)
            return True
        except urllib2.URLError as err: pass
        return False

    def set_provider(self, provider):
        self.provider = provider

    def exit_thread(self):
        self._exit_thread = True

    def send_sms(self):
        self._sms_to_send = True

    def run(self):
        while not self._exit_thread:                 
            time.sleep(self.sender.thread_sleep_time)
            check_connection()
        #end_while    
        #print "Exit from Thread!!!"

