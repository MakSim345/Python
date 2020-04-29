#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
## Info:
## https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
##
#############################################################################

import time
import sys
import telebot

import json
import requests

from telegram_auth import user_token

sys.path.insert(0, '/home/ys/dev/scripts/temp_warning_sms')
from temperature_warning_unit import check_frozen_condition

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


URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message_once(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    _result = get_url(url)

# main entrance point:
if __name__ == '__main__':

    chat_id = u_token.chat_id
    print "chat_id:", chat_id

    # ATTN! use follow: .encode('utf-8') for prevent
        # UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0'
        # in position 20: ordinal not in range(128)

    _condition = -25

    #test:
    #_condition = 5

    chk = check_frozen_condition(_condition)
    text_to_send = chk.check_condition()

    if (text_to_send):
        timestamp = tlg_timestamp()
        text_to_send = timestamp.get_timestamp() + "\n" + text_to_send
        print "Message to send:"
        print text_to_send
        print "--------------------------------"
        send_message_once(text_to_send, chat_id)
    else:
        print "Temperature is warmer than ", _condition

