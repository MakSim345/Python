#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os
import urllib2
from google_auth import userpass
import time
import smtplib
import traceback
from translate_conditions import text_utils
from logger import logEngine

class sendSMS(): 
    def __init__(self, provider='GMAIL', new_subj = '-'):
        self.u_pass = userpass()
        # choose mail provider:
        if provider=='GMAIL':
            self.u_pass.gmail_provider()
        elif provider == 'YANDEX':
            self.u_pass.yandex_provider()
        elif provider == 'YAHOO':
            self.u_pass.yahoo_provider()    
        
        self.init_provider()

        self._internal_loop = True
        self._loop_counter = 0
        self._number_of_try = 1
        self.to_yuriy = self.u_pass.to_yuriy
        self.to_mama =self.u_pass.to_mama
        self.to_my_gmail = self.u_pass.to_my_gmail
        self.to_tolik_gmail = "senishcht@gmail.com"
        self.recepient = self.to_mama
        self.set_subj_for_mail (new_subj)
        self.set_from_for_mail('Po6oT')

    def set_subj_for_mail(self, _subj):
        self.subj = _subj
    
    def set_from_for_mail(self, _from_str):
        self._from = _from_str

    def init_provider(self): 
        self.HOST = self.u_pass.HOST
        self.PORT = self.u_pass.PORT   
        self.ACCOUNT =  self.u_pass.ACCOUNT #put your gmail email account name here
        self.PASSWORD = self.u_pass.PASSWORD # put your gmail email account password here
    
    def send_info_sms(self, msg_body):
        #msg = self._text_utils.replace_chars(msg)
        russian = 'windows-1251'
        # m = 'Текст сообщения'
        # Указываем кодировку  
        # msg_body = MIMEText(msg, "", "utf-8")  
        msg = MIMEMultipart()
        msg["Subject"] = Header(self.subj, russian)
        msg["From"] = Header(self._from, russian)
        msg["To"] = Header(self.recepient, russian)
        
        # m = """привет от Васи"""
        
        # text = MIMEText(msg_body, 'plain', 'UTF-8')
        text = MIMEText(msg_body, 'plain', 'utf-8')
        #text = MIMEText(m, 'plain', 'UTF-8')
        
        msg.attach(text)
        
        while(self._internal_loop):
            try:
                server = smtplib.SMTP(self.HOST, self.PORT)            
                #server.set_debuglevel(1)    # you don't need this
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.ACCOUNT, self.PASSWORD)
                
                #server.sendmail(self.ACCOUNT, self.recepient, msg.as_string())
                #print "SMS sent to", self.recepient, "via", self.ACCOUNT
                
                #server.sendmail(self.ACCOUNT, self.to_yuriy, msg.as_string())
                #print "SMS sent to", self.to_yuriy, "via", self.ACCOUNT
                
                self.recepient = self.to_mama
                server.sendmail(self.ACCOUNT, self.recepient, msg.as_string())
                print "SMS sent to", self.recepient, "via", self.ACCOUNT
                
                self.recepient = self.to_tolik_gmail
                server.sendmail(self.ACCOUNT, self.recepient, msg.as_string())
                print "SMS sent to", self.recepient, "via", self.ACCOUNT
                
                self.recepient = self.to_my_gmail
                server.sendmail(self.ACCOUNT, self.to_my_gmail, msg.as_string())
                print "SMS sent to", self.to_my_gmail, "via", self.ACCOUNT
                   
                server.quit()
                self._internal_loop = False
            except:
                traceback.print_exc()
                time.sleep(2)
                self._loop_counter += 1
                print "Try to send SMS ", self._loop_counter , "times from", self._number_of_try 
                if self._loop_counter >= self._number_of_try:
                    print "ERROR: Failed sending", self._number_of_try, " times SMS to", self.recepient, "via", self.ACCOUNT
                    self._internal_loop = False


# main entrance point:
if __name__ == "__main__":
    _ATTN = ""
    _ATTN_SOON   = "BHuMaHue! y Bac CKOPO Bo3Mo*Ho npeBbIweHue LuMuTa!"
    _ATTN_LATE   = "BHuMaHue! y Bac npeBbIweHue LuMuTa TpaFFuka Ha "
    _iRobot = ". PEOPLENET (po6oT)."

    log = logEngine()

    all_the_text = "!!!!"

    try:
        sender =  sendSMS('YANDEX')
        _result_int = 2

        if (_result_int > 0):
            _ATTN = _ATTN_SOON
        else:
            _ATTN = _ATTN_LATE
        #endif

        _result_traffic = _ATTN + _iRobot
        print _result_traffic
        result = sender.send_info_sms(_result_traffic)

    except:
        traceback.print_exc()
        a ="ERROR: Failed sending SMS!"
        print a
        log.saveMessageToLog(a)
        time.sleep(1)
