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
    
u_token = user_token()
TOKEN = u_token.token

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telebot.TeleBot(TOKEN)

# polling does not work for now. 2019-JUN
# bot.polling(none_stop=True, interval=0)

# @bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


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

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_timestamp(_selector = "date"):

        _day = time.strftime("%d")
        _year = time.strftime("%Y")
        _month = time.strftime("%m")

        # _date = _year + '-' +  self.mth_str.get_month(int(_month)) + '-' +  _day
        _date = _year + '-' +  _month + '-' +  _day
        _time = time.strftime("%H:%M:%S")

        if _selector == "time":
             return _time
        else:
            return _date


if __name__ == '__main__':
    # test_02()
    text = "empty"
    chat = "12345"
    chat_id = u_token.chat_id
    #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    # bot.send_message(chat_id, "Привет, чем я могу тебе помочь?")
    # bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.")
    #bot.send_message("Привет, чем я могу тебе помочь?")
    # text, chat = get_last_chat_id_and_text(get_updates())
    print "text:", text
    print "chat:", chat
    # text = "Привет, чем я могу тебе помочь?"
    # text_to_send = "Я тебя не понимаю. Напиши /help."
    text_to_send = get_timestamp()
    send_message(text_to_send, chat_id)
    # send_message(chat_id, "Я тебя не понимаю. Напиши /help.")


