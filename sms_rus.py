#!/usr/bin/env python
# -*- coding: utf8 -*-

import urllib2
import smtplib
import traceback
from google_auth import userpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email.utils  
import time

#from weather_unit import weather_city
#from translate_conditions import text_utils

class sendSMS(): 
    def __init__(self, provider='GMAIL', new_subj = '-'):
        self.u_pass = userpass()
        # choose mail provider:
        if provider=='GMAIL':
            self.u_pass.gmail_provider()
        elif provider == 'YANDEX':
            self.u_pass.yandex_provider()
        
        self.init_provider()

        self._internal_loop = True
        self._loop_counter = 0
        self._number_of_try = 1
        self.to_yuriy = self.u_pass.to_yuriy
        self.to_mama =self.u_pass.to_mama
        self.to_my_gmail = self.u_pass.to_my_gmail
        self.recepient = self.to_mama
        self.set_subj_for_mail (new_subj)
        #self._text_utils = text_utils()

    def set_subj_for_mail(self, _subj):
        self.subj = _subj

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
        msg["From"] = Header('Po6oT', russian)
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
        
class logEngine(): 
    def __init__(self):
        self._log_file_name = 'log_Hki_sms_weather.log'

    def saveMessageToLog(self, _text):        
        file = open(self._log_file_name, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("Message:\n")
        file.write(_text)
        file.write("-------------------------------------\n")
        file.close()

# main entrance point:
if __name__ == "__main__":
    _hki_url = "http://www.foreca.com/Finland/Helsinki?tenday"

    try:
        sender =  sendSMS('YANDEX')
        #sender =  sendSMS('GMAIL')
    
        weather = weather_city()
        weather.set_city_url(_hki_url)
        #result = sender.send_info_sms(weather.get_weather_for_city())

        stMess = "О, сколько нам открытий чудных готовит просвещенья дух. "
        #print stMess

        # stMess = MIMEText(testMess, _charset="cp1251")
        result = sender.send_info_sms(stMess)
        
    except:
        traceback.print_exc()
        log = logEngine()
        a ="ERROR: Failed sending SMS about HKI weather!" 
        print a
        log.saveMessageToLog(a)
        time.sleep(1)
