#!/usr/bin/python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

import os, sys
import time
import socket
import struct
from platform import system
import requests

#telegram:
import telebot
from telegram_auth import user_token

u_token = user_token()
TOKEN = u_token.token

class tlg_timestamp():
    def __init__(self):
        ''' init class'''
        STR_JAN="JAN"
        STR_FEB="FEB"
        STR_MAR="MAR"
        STR_APR="APR"
        STR_MAY="MAY"
        STR_JUN="JUN"
        STR_JUL="JUL"
        STR_AUG="AUG"
        STR_SEP="SEP"
        STR_OCT="OCT"
        STR_NOV="NOV"
        STR_DEC="DEC"
        self._month_str = {1:STR_JAN, 2:STR_FEB, 3:STR_MAR, 4:STR_APR,
                           5:STR_MAY, 6:STR_JUN, 7:STR_JUL, 8:STR_AUG,
                           9:STR_SEP, 10:STR_OCT, 11:STR_NOV, 12:STR_DEC}

    def get_month(self, month_int):
        '''return month in str'''
        return self._month_str.get(int(month_int))

    def get_timestamp(self, _selector = ""):
        _day = time.strftime("%d")
        _year = time.strftime("%Y")
        _month = time.strftime("%m")

        # use string for month representation:
        _date = _year + '-' +  self.get_month(int(_month)) + '-' +  _day

        # month in digital format:
        # _date = _year + '-' +  _month + '-' +  _day

        _time = time.strftime("%H:%M:%S")

        if _selector == "time":
            return _time
        elif _selector == "date":
            return _date
        else:
            return _date + " " + _time

def get_ip_address(ifname):
    local_os = system()
    if local_os == 'Linux':
        import fcntl
    elif local_os == 'Windows':
        # print "OS - Windows. Module 'fcntl' not supported!"
        return socket.gethostbyname(socket.gethostname())

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        retValue = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15]))[20:24])
    except:
        retValue = "IP: "+ifname+" not exists!"

    # print retValue
    return retValue


def get_local_os():
    local_os = system()
    if local_os == 'Linux':
        retValue = "OS - Linux"
    elif local_os == 'Windows':
        retValue = "OS - Windows. Module 'fcntl' not supported!"
    return retValue


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message_once(text, chat_id):
    URL = "https://api.telegram.org/bot{}/".format(TOKEN)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    _result = get_url(url)

def saveMessageToLog(_my_text):
    _log_file_name = 'IP_address_sms.log'
    file = open(_log_file_name, "a")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
    file.write("Message:\n" + _my_text)
    file.write("\n-------------------------------------\n")
    file.close()

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    time.sleep(15)

    chat_id = u_token.chat_id
    print "chat_id:", chat_id
   
    #run in current directory:
    cwd = os.getcwd()
    os.chdir(cwd)
    sys.path[0]

    _retVal = ' '
    
    _retVal = "ys-server restarted now\n"
    # _retVal = "INFO: YS-SERVER " + time.strftime("%H:%M:%S %Y-%m-%d\n")
    _main_info_str = _retVal + get_local_os()
    
    my_interfaces_list =  os.listdir('/sys/class/net/') 
    
    # print get_local_os() 
    for _network_if in my_interfaces_list:
        # print _network_if
        _ip_address = get_ip_address(_network_if)
        _main_info_str = _main_info_str + '\nIP address ' +_network_if +':\n' + _ip_address
    #end_for

    # print _main_info_str

    if (_main_info_str):
        timestamp = tlg_timestamp()
        _main_info_str = timestamp.get_timestamp() + "\n" + _main_info_str
        print "Message to send:"
        print _main_info_str
        print "--------------------------------"
        send_message_once(_main_info_str, chat_id)
    else:
        print "Nothing to send. "
