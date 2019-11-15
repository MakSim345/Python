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



# @bot.message_handler(commands=['start'])
# def start_message(message):
#    bot.send_message(message.chat.id, "Привет, ты написал мне /start")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # DEBUG: 
    # print "get_text_message - enter."
    if message.text.lower() == "/help":
        bot.send_message(message.chat.id, "Напиши /start")
    elif message.text.lower()  == "/start":
        bot.send_message(message.chat.id, "Привет, ты написал мне /start")
    elif message.text.lower()  == "time":
        bot.send_message(message.chat.id, get_timestamp())
    elif message.text.lower()  == 'Hello':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower()  == 'Bye':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")


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
    bot.polling(none_stop=True)
    #bot.polling()

